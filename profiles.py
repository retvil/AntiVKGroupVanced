"""Product profiles for the AntiVKGroup editions.

One codebase, two products:
- VANCED   — Mail.ru Agent + VK Messenger removal (the classic edition)
- EXTENDED — removal of every Mail.ru / VK Group product (superset of
  VANCED: Облако Mail.ru shell integration, leftover data directories,
  hosts/firewall/Defender traces, Store apps, game launchers)
"""

VANCED = "vanced"
EXTENDED = "extended"

PRODUCT_NAMES: dict[str, str] = {
    VANCED: "AntiVKGroupVanced",
    EXTENDED: "AntiVKGroupExtended",
}

# Ordered scan steps for the EXTENDED profile (superset, canonical order).
_EXTENDED_STEPS: tuple[str, ...] = (
    "scan_install_paths",
    "scan_uninstall_entries",
    "scan_default_browser",
    "scan_mailto_hijack",
    "scan_start_page",
    "scan_start_menu_internet",
    "scan_software_keys",
    "scan_policy_hijack",
    "scan_startup_urls",
    "scan_chromium_profiles",
    "scan_web_data_keywords",
    "scan_firefox_search",
    "scan_firefox_homepage",
    "scan_search_scopes",
    "scan_autostart",
    "scan_scheduled_tasks",
    "scan_services",
    "scan_file_associations",
    "scan_zone_map",
    "scan_registered_apps",
    "scan_shell_overlays",
    "scan_context_menus",
    "scan_startup_approved",
    "scan_app_paths",
    "scan_shortcuts",
    "scan_leftover_dirs",
    "scan_hosts",
    "scan_firewall_rules",
    "scan_uri_protocols",
    "scan_browser_extensions",
    "scan_cookies",
    "scan_openwith",
    "scan_traces",
    "scan_muicache",
    "scan_defender_exclusions",
    "scan_store_apps",
    "scan_product_dirs",
    "scan_local_data_dirs",
)

# Steps that go beyond messenger+search and belong to the Extended edition only.
_EXTENDED_ONLY: frozenset[str] = frozenset({
    "scan_shell_overlays",       # Облако Mail.ru Explorer integration
    "scan_context_menus",        # Облако Mail.ru Explorer integration
    "scan_leftover_dirs",        # ProgramData / Roaming / Облако Mail.ru data
    "scan_hosts",
    "scan_firewall_rules",
    "scan_defender_exclusions",
    "scan_store_apps",           # VK / Mail.ru / ICQ / TamTam Store (Appx) apps
    "scan_product_dirs",         # Program Files\Mail.Ru / VK non-messenger products
    "scan_local_data_dirs",      # %LOCALAPPDATA%\Mail.Ru / VK non-messenger data
})

PROFILE_SCANS: dict[str, tuple[str, ...]] = {
    EXTENDED: _EXTENDED_STEPS,
    VANCED: tuple(s for s in _EXTENDED_STEPS if s not in _EXTENDED_ONLY),
}


def validate(profile: str) -> str:
    """Return the profile name if known, raise ValueError otherwise."""
    if profile not in PROFILE_SCANS:
        raise ValueError(f"unknown profile: {profile!r}")
    return profile
