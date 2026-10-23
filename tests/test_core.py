"""Unit tests for pure logic: engine lookup, Firefox policies.json, LZ4 decompressor.

No GUI, no registry, no network — everything runs on CPU in milliseconds.
"""

import json
import struct

import pytest

import engines
import mailru_detect
import policies
import profiles


# --- engines -------------------------------------------------------------------

def test_get_engine_returns_matching_engine():
    engine = engines.get_engine("DuckDuckGo")
    assert engine.name == "DuckDuckGo"
    assert "duckduckgo.com" in engine.search_url


def test_get_engine_unknown_name_raises_keyerror():
    with pytest.raises(KeyError):
        engines.get_engine("Mail.ru")


def test_all_engines_have_unique_names_and_valid_urls():
    names = [e.name for e in engines.SEARCH_ENGINES]
    assert len(names) == len(set(names))
    for engine in engines.SEARCH_ENGINES:
        assert "{searchTerms}" in engine.search_url
        assert engine.search_url.startswith("https://")


# --- Firefox policies.json -----------------------------------------------------

def test_firefox_policies_json_with_suggest_url():
    engine = engines.get_engine("Google")
    doc = policies._firefox_policies_json(engine)
    entry = doc["policies"]["SearchEngines"]["Add"][0]
    assert entry["Name"] == "Google"
    assert "SuggestURLTemplate" in entry


def test_firefox_policies_json_without_suggest_url_has_no_null():
    engine = engines.SearchEngine(
        name="Custom", keyword="custom", search_url="https://c.example/?q={searchTerms}"
    )
    doc = policies._firefox_policies_json(engine)
    entry = doc["policies"]["SearchEngines"]["Add"][0]
    assert "SuggestURLTemplate" not in entry
    # document must be JSON-serializable without nulls in the engine entry
    serialized = json.dumps(doc)
    assert "null" not in serialized


# --- LZ4 block decompressor ----------------------------------------------------

def _lz4_compress_literals_only(data: bytes) -> bytes:
    """Minimal LZ4 compressor: literals-only blocks (no matches)."""
    out = bytearray()
    src = 0
    while src < len(data):
        chunk = data[src:src + 65535]
        lit_len = len(chunk)
        token = (lit_len if lit_len < 15 else 15) << 4
        out.append(token)
        if lit_len >= 15:
            remaining = lit_len - 15
            while remaining >= 255:
                out.append(255)
                remaining -= 255
            out.append(remaining)
        out += chunk
        src += lit_len
    out.append(0)  # end mark: empty token
    return bytes(out)


def test_lz4_decompress_literals_only_roundtrip():
    original = b"Hello, Mail.ru removal!" * 100
    compressed = _lz4_compress_literals_only(original)
    size = len(original)
    result = mailru_detect._lz4_block_decompress(compressed, size)
    assert result == original


def test_lz4_decompress_with_match():
    # "abc" literals + match(offset=3, len=6) -> "abcabcabc"
    token = (3 << 4) | 2  # literal_len=3, match_len=2 (+4 => 6)
    block = bytes([token]) + b"abc" + struct.pack("<H", 3)
    assert mailru_detect._lz4_block_decompress(block, 9) == b"abcabcabc"


def test_lz4_decompress_corrupt_offset_raises():
    # token with literal_len=0, match_len=0; offset=0 is invalid
    block = bytes([0x00]) + struct.pack("<H", 0)
    with pytest.raises(ValueError):
        mailru_detect._lz4_block_decompress(block, 100)


# --- markers -------------------------------------------------------------------

def test_is_mailru_positive_markers():
    for text in (
        "Mail.ru Agent", "агент mail.ru", "VK Messenger", "VK Мессенджер",
        "ICQ", "TamTam", "Облако Mail.ru", "https://go.mail.ru/search",
        "VK Play", "My.com GameCenter", "vk", "icq", "tamtam",
    ):
        assert mailru_detect._is_mailru(text), text


def test_is_mailru_negative():
    for text in ("Google Chrome", "Mozilla Firefox", "https://google.com", ""):
        assert not mailru_detect._is_mailru(text), text


# --- scheduled tasks parsing ---------------------------------------------------

def test_decode_schtasks_utf8():
    assert mailru_detect._decode_schtasks("TaskName,Status\n".encode("utf-8")) == "TaskName,Status\n"


def test_scan_scheduled_tasks_handles_missing_schtasks(monkeypatch):
    def boom(*args, **kwargs):
        raise FileNotFoundError("schtasks")
    monkeypatch.setattr(mailru_detect.subprocess, "run", boom)
    assert mailru_detect.scan_scheduled_tasks() == []


# --- exclusions ----------------------------------------------------------------

def test_exclusions_roundtrip(tmp_path, monkeypatch):
    import exclusions
    monkeypatch.setattr(exclusions, "EXCLUSIONS_FILE", tmp_path / "exclusions.json")
    monkeypatch.setattr(exclusions, "BASE_DIR", tmp_path)
    assert exclusions.load() == set()
    exclusions.add("Service: MailRuUpdaterService (Mail.ru Updater)")
    assert exclusions.is_excluded("Service: MailRuUpdaterService (Mail.ru Updater)")
    assert not exclusions.is_excluded("Scheduled task: MailRuAgentAutoRun")
    exclusions.clear()
    assert exclusions.load() == set()


def test_exclusions_load_corrupt_file_returns_empty(tmp_path, monkeypatch):
    import exclusions
    bad = tmp_path / "exclusions.json"
    bad.write_text("{not json", encoding="utf-8")
    monkeypatch.setattr(exclusions, "EXCLUSIONS_FILE", bad)
    assert exclusions.load() == set()


# --- extended vectors ----------------------------------------------------------

def test_lnk_mentions_mailru_ascii_and_utf16(tmp_path):
    plain = tmp_path / "plain.lnk"
    plain.write_bytes(b"\x00\x01chrome" + b"\x00" * 32)
    assert not mailru_detect._lnk_mentions_mailru(plain)
    ascii_lnk = tmp_path / "ascii.lnk"
    ascii_lnk.write_bytes(b"\x00\x01" + b"C:\\Mail.Ru\\agent.exe" + b"\x00" * 8)
    assert mailru_detect._lnk_mentions_mailru(ascii_lnk)
    utf16_lnk = tmp_path / "utf16.lnk"
    utf16_lnk.write_bytes(b"\x00\x01" + "Агент Mail.ru".encode("utf-16-le"))
    assert mailru_detect._lnk_mentions_mailru(utf16_lnk)


def test_hosts_mailru_lines_skips_comments_and_other_domains():
    text = "\n".join([
        "# comment mail.ru",
        "127.0.0.1 mail.ru",
        "  0.0.0.0 go.mail.ru  ",
        "1.2.3.4 google.com",
        "",
    ])
    lines = mailru_detect._hosts_mailru_lines(text)
    assert lines == ["127.0.0.1 mail.ru", "0.0.0.0 go.mail.ru"]


def test_parse_firewall_output():
    text = "\nRule1|Display One\n\nRule2|Display Two\n|\n"
    assert mailru_detect._parse_firewall_output(text) == [
        ("Rule1", "Display One"),
        ("Rule2", "Display Two"),
    ]


def test_consent_prefixes_cover_consent_findings():
    samples = [
        "Roaming: C:\\Users\\X\\AppData\\Roaming\\Mail.Ru",
        "Cloud files: C:\\Users\\X\\Облако Mail.ru",
        "Local data: C:\\Users\\X\\AppData\\Local\\Mail.Ru\\Games",
        "Extension: C:\\Users\\X\\...\\Extensions\\abc",
        "Cookies: Google Chrome [Default] (3 rows)",
        "Defender exclusion: C:\\Mail.Ru",
    ]
    for sample in samples:
        assert sample.startswith(mailru_detect.CONSENT_PREFIXES), sample


def test_new_scan_functions_return_lists():
    for name in (
        "scan_shell_overlays", "scan_context_menus", "scan_startup_approved",
        "scan_app_paths", "scan_shortcuts", "scan_leftover_dirs", "scan_hosts",
        "scan_firewall_rules", "scan_uri_protocols", "scan_browser_extensions",
        "scan_cookies", "scan_openwith", "scan_traces",
        "scan_defender_exclusions",
    ):
        assert isinstance(getattr(mailru_detect, name)(), list), name


# --- product profiles (Vanced / Extended) ---------------------------------------

def test_profile_steps_reference_existing_scan_functions():
    for profile, steps in profiles.PROFILE_SCANS.items():
        for name in steps:
            assert callable(getattr(mailru_detect, name, None)), (profile, name)


def test_extended_is_superset_of_vanced():
    assert set(profiles.PROFILE_SCANS[profiles.VANCED]) < set(
        profiles.PROFILE_SCANS[profiles.EXTENDED]
    )


def test_vanced_excludes_product_wide_vectors():
    vanced = set(profiles.PROFILE_SCANS[profiles.VANCED])
    for name in (
        "scan_shell_overlays", "scan_context_menus", "scan_leftover_dirs",
        "scan_hosts", "scan_firewall_rules", "scan_defender_exclusions",
        "scan_store_apps", "scan_product_dirs", "scan_local_data_dirs",
    ):
        assert name not in vanced, name


def test_validate_rejects_unknown_profile():
    with pytest.raises(ValueError):
        profiles.validate("nope")


def test_scan_all_vanced_runs_and_is_list():
    assert isinstance(mailru_detect.scan_all(profiles.VANCED), list)


def test_scan_all_default_is_extended():
    import inspect
    signature = inspect.signature(mailru_detect.scan_all)
    assert signature.parameters["profile"].default is None


# --- Extended product scans (Store apps, product dirs) ---------------------------

def test_parse_appx_output():
    import products_detect
    text = "VK|VK_1.2.3_x64__abc123\n\njunk\n|"
    parsed = products_detect._parse_appx_output(text)
    assert parsed == [("VK", "VK_1.2.3_x64__abc123")]


def test_scan_store_apps_returns_list():
    import products_detect
    assert isinstance(products_detect.scan_store_apps(), list)


def test_scan_product_dirs_includes_local_programs(tmp_path, monkeypatch):
    import products_detect
    programs = tmp_path / "Programs"
    (programs / "VKPlay").mkdir(parents=True)
    (programs / "VK" / "Agent").mkdir(parents=True)
    (programs / "VK" / "Cloud").mkdir(parents=True)
    (programs / "OtherApp").mkdir()
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    found = products_detect.scan_product_dirs()
    assert any(f.endswith("VKPlay") for f in found)
    assert any(f.endswith("Cloud") for f in found)
    assert not any(f.endswith("Agent") for f in found)
    assert not any("OtherApp" in f for f in found)


def test_remove_one_store_app_and_product_dir_dispatch(monkeypatch):
    import products_detect
    calls = []
    monkeypatch.setattr(
        products_detect, "remove_store_app",
        lambda finding: calls.append("store") or True,
    )
    monkeypatch.setattr(
        products_detect, "remove_product_dir",
        lambda finding: calls.append("dir") or True,
    )
    removed: list[str] = []
    failed: list[str] = []
    mailru_detect._remove_one("Store app: VK (VK_1.0_x64__abc)", removed, failed)
    mailru_detect._remove_one("Product dir: C:\\Program Files\\VK\\Play", removed, failed)
    assert calls == ["store", "dir"]
    assert failed == []
    assert removed == ["VK (VK_1.0_x64__abc)", "C:\\Program Files\\VK\\Play"]


def test_is_product_process_matches_products():
    import products_detect
    assert products_detect.is_product_process("magent.exe") is True
    assert products_detect.is_product_process("icq.exe") is True
    assert products_detect.is_product_process("cloud.exe") is True
    assert products_detect.is_product_process("MailRuUpdater.exe") is True
    assert products_detect.is_product_process("vkplay.exe") is True
    assert products_detect.is_product_process("chrome.exe") is False
    assert products_detect.is_product_process("agent-browser-win32-x64.exe") is False
    assert products_detect.is_product_process(None) is False
    assert products_detect.is_product_process("") is False


def test_scan_local_data_dirs_skips_messenger(tmp_path, monkeypatch):
    import products_detect
    base = tmp_path / "Mail.Ru"
    (base / "Agent").mkdir(parents=True)
    (base / "Games").mkdir()
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    found = products_detect.scan_local_data_dirs()
    assert found == [f"Local data: {base / 'Games'}"]


def test_consent_prefixes_cover_local_data():
    assert "Local data: " in mailru_detect.CONSENT_PREFIXES


# --- Start Page vector -----------------------------------------------------------

def test_scan_start_page_returns_list():
    assert isinstance(mailru_detect.scan_start_page(), list)


def test_start_page_in_both_editions():
    assert "scan_start_page" in profiles.PROFILE_SCANS[profiles.VANCED]
    assert "scan_start_page" in profiles.PROFILE_SCANS[profiles.EXTENDED]


# --- Startup URLs and Firefox homepage vectors -----------------------------------

def test_scan_startup_urls_returns_list():
    assert isinstance(mailru_detect.scan_startup_urls(), list)


def test_scan_firefox_homepage_returns_list():
    assert isinstance(mailru_detect.scan_firefox_homepage(), list)


def test_startup_urls_and_firefox_homepage_in_both_editions():
    for name in ("scan_startup_urls", "scan_firefox_homepage"):
        assert name in profiles.PROFILE_SCANS[profiles.VANCED]
        assert name in profiles.PROFILE_SCANS[profiles.EXTENDED]


def test_remove_firefox_homepage_strips_mailru_lines(tmp_path, monkeypatch):
    profile_dir = tmp_path / "abc.default"
    profile_dir.mkdir()
    prefs = profile_dir / "prefs.js"
    prefs.write_text(
        'user_pref("browser.startup.homepage", "https://go.mail.ru/");\n'
        'user_pref("browser.startup.homepage_override.mstone", "138.0");\n'
        'user_pref("browser.startup.page", 1);\n',
        encoding="utf-8",
    )
    monkeypatch.setattr(
        mailru_detect, "_firefox_profile_roots", lambda: [tmp_path]
    )
    assert mailru_detect._remove_firefox_homepage("abc.default") is True
    kept = prefs.read_text(encoding="utf-8")
    assert "go.mail.ru" not in kept
    assert "browser.startup.homepage_override.mstone" in kept
    assert "browser.startup.page" in kept


def test_remove_one_startup_url_dispatch(monkeypatch):
    calls = []
    monkeypatch.setattr(
        mailru_detect, "_remove_startup_urls",
        lambda browser: calls.append(browser) or True,
    )
    removed: list[str] = []
    failed: list[str] = []
    mailru_detect._remove_one("Startup URL: Edge https://go.mail.ru/", removed, failed)
    assert calls == ["Edge"]
    assert removed == ["Edge https://go.mail.ru/"]
    assert failed == []


# --- Zone map, RegisteredApplications and MUICache vectors -----------------------

def test_scan_zone_map_returns_list():
    assert isinstance(mailru_detect.scan_zone_map(), list)


def test_scan_registered_apps_returns_list():
    assert isinstance(mailru_detect.scan_registered_apps(), list)


def test_scan_muicache_returns_list():
    assert isinstance(mailru_detect.scan_muicache(), list)


def test_new_registry_scans_in_both_editions():
    for name in ("scan_zone_map", "scan_registered_apps", "scan_muicache"):
        assert name in profiles.PROFILE_SCANS[profiles.VANCED]
        assert name in profiles.PROFILE_SCANS[profiles.EXTENDED]


def test_remove_one_zone_map_registered_muicache_dispatch(monkeypatch):
    calls: list[tuple] = []
    monkeypatch.setattr(
        mailru_detect, "_delete_tree_any_hive",
        lambda path: calls.append(("tree", path)) or True,
    )
    monkeypatch.setattr(
        mailru_detect, "_delete_value_any_hive",
        lambda path, name: calls.append(("value", path, name)) or True,
    )
    removed: list[str] = []
    failed: list[str] = []
    mailru_detect._remove_one("Zone map: mail.ru", removed, failed)
    mailru_detect._remove_one(
        "Registered app: Агент Mail.ru = Software\\Mail.Ru\\Capabilities",
        removed, failed,
    )
    mailru_detect._remove_one("MUICache: magent.exe", removed, failed)
    assert calls[0][0] == "tree" and calls[0][1].endswith("mail.ru")
    assert calls[1] == (
        "value", mailru_detect._REGISTERED_APPS_KEY, "Агент Mail.ru"
    )
    assert calls[2] == ("value", mailru_detect._MUICACHE_KEY, "magent.exe")
    assert len(removed) == 3
    assert failed == []
