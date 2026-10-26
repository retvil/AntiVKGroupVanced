# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-10-22

Initial release of **AntiVKGroupVanced** — a Mail.ru / VK removal tool for
Windows, a companion project to [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Added

- Two editions from one codebase: **AntiVKGroupVanced** (Mail.ru Agent +
  VK Messenger removal) and **AntiVKGroupExtended** (every Mail.ru / VK
  product) — product profiles in `profiles.py` select the scan scope, shared
  GUI in `app.py`, thin entry points `main.py` / `main_extended.py`
- **Search hijack scanner** — detects 37 vectors Mail.ru / VK software uses
  to install itself as default search/browser:
  - running processes (Agent, VK Messenger, Cloud Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - installation directories on disk
  - uninstall registry entries (HKLM, WOW6432Node, HKCU)
  - `StartMenuInternet` browser client registrations
  - standalone `Software\Mail.Ru` key trees (HKCU/HKLM/WOW6432Node)
  - enterprise-policy hijack via `DefaultSearchProvider*` registry values
  - per-profile Chromium `Preferences` JSON (Chrome, Edge, Brave, Vivaldi, Opera)
  - search-engine keyword rows in Chromium `Web Data` SQLite databases
  - Firefox/Waterfox `search.json.mozlz4` (with a built-in pure-Python LZ4
    block decompressor)
  - legacy IE/Windows `SearchScopes` entries
  - autostart entries (`Run`/`RunOnce`)
  - Windows Task Scheduler entries (Mail.ru updater tasks)
  - Windows services (registry-based scan, `sc stop` + `sc delete` removal)
  - file associations (`FileExts\<ext>\UserChoice` ProgId scan + removal)
  - shortcuts (Desktop / Start Menu / taskbar)
  - leftover directories (ProgramData, Roaming)
  - `hosts` entries
  - Windows Firewall rules
  - URI protocol handlers
  - browser extensions (Chromium manifests + Firefox `.xpi`)
  - mail.ru cookies (Chromium + Firefox)
  - `OpenWithProgids`/`OpenWithList` associations
  - Prefetch / CrashDumps / WER traces
  - Windows Defender exclusions
  - IE Start Page hijack (`Internet Explorer\Main\Start Page`)
  - startup-URL policy hijack (`RestoreOnStartupURLs` in Edge, Chrome,
    Chromium, Brave, Vivaldi, Opera)
  - Firefox homepage hijack (`browser.startup.homepage` in `prefs.js`)
  - IE zone-map entries for Mail.ru domains
  - RegisteredApplications entries
  - MUICache execution traces
  - %TEMP% installer traces
  - Extended only: shell icon overlays and context-menu handlers
  - Extended only: Store (Appx) apps — ICQ, TamTam, VK Play and other
    Mail.ru / VK Store apps, removed via `Remove-AppxPackage`
  - Extended only: non-browser product directories under `Program Files\`
    (Cloud Mail.ru, My.com, ...) with backup-before-delete removal
  - Extended only: non-browser local data directories under `%LOCALAPPDATA%\`
    — consent-gated, backed up before deletion
- **Hijack removal** — one-click removal of every detected vector, with
  per-vector removers; locked databases/files (browser running) are reported,
  never crash
- **Hard default-search policy** — enforces one of 10 search engines
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - Chromium family via HKLM `SOFTWARE\Policies\...` `DefaultSearchProvider*`
    values (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox via `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- **Remove Mail.ru policies** button — strips Mail.ru `DefaultSearchProvider*`
  policy values from the registry
- **User data consent** — findings that touch personal data (Cloud Mail.ru
  files, ICQ/TamTam history, extensions, cookies, Defender exclusions)
  require an explicit extra confirmation before removal
- **Selection dialog** after scan: pick exactly which findings to remove
  instead of all-or-nothing removal
- **Exclusions**: unchecked findings can be saved to
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — future scans deselect them
  automatically, but they stay selectable in the dialog; exclusions can be
  reset from the dialog
- **Backup before removal**: every registry key / profile file touched is
  exported to `%APPDATA%\AntiVKGroupVanced\backup\<timestamp>\` before deletion
- **Operation log**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 UI languages** (ru, en, uk, kk, de, fr, es, pl, tr, zh) in a dedicated
  `translations.py` module; system language auto-detected via Windows UI
  language API (`GetUserDefaultUILanguage`), English fallback when no match
- **Light UI** on ttkbootstrap (`flatly` theme): vertical window layout,
  centered action stack, full-width section cards, pinned status bar and
  footer with author, version and clickable GitHub link
- Administrator-rights check at startup with a warning in the status bar
- Prompt to close running browsers before hijack removal (prevents
  "database locked")
- "Open report folder" offer when some hijack items fail to be removed
- `build.bat` builds both edition EXEs (PyInstaller, `--onefile --windowed`)
- Unit tests for pure logic: engine lookup, Firefox `policies.json`, LZ4
  decompressor, `.lnk` byte detection, hosts-line filtering, firewall output
  parsing, consent-prefix coverage, exclusions persistence, per-vector
  removal dispatch, profile definitions

[Unreleased]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
