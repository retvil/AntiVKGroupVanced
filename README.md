# AntiVKGroup Vanced

[![1.0.0](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Remove Mail.ru and VK software completely and lock your default search against hijacking — 29 detection vectors (VANCED) / 38 detection vectors (EXTENDED), 10 search engines, 10 UI languages.**

## 🌐 Languages

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)



## What is this?

Mail.ru (VK Group) doesn't just install its apps — Agent, VK Messenger, Cloud Mail.ru and the go.mail.ru search quietly register themselves through dozens of system mechanisms: registry associations, enterprise policies, per-profile browser settings, even search-engine databases inside Chromium profiles. Uninstalling the apps alone doesn't undo all of that.

**AntiVKGroup Vanced** (a fork of [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex)) finds **all hijack vectors** (29 in VANCED, 38 in EXTENDED), removes them with one click, and then **hard-locks your default search** to an engine of your choice via Windows enterprise policies — so nothing can silently take it back.

## Features

- **Hijack scanner** — detects 29 vectors (VANCED) / 38 vectors (EXTENDED): install paths, uninstall registry entries, `StartMenuInternet` registrations, `Software\Mail.Ru` key trees, `DefaultSearchProvider*` policy hijack, Chromium profile `Preferences`, `Web Data` SQLite keywords, Firefox `search.json.mozlz4`, legacy `SearchScopes`, autostart entries, scheduled tasks, Windows services, shortcuts, ProgramData/Roaming leftovers, hosts entries, firewall rules, URI protocols, browser extensions, mail.ru cookies, open-with associations, Prefetch/WER traces, Defender exclusions, IE Start Page hijack, startup-URL policies (`RestoreOnStartupURLs`), Firefox homepage, IE zone map, RegisteredApplications entries, MUICache traces, %TEMP% installers — plus, in the Extended edition: shell overlays, context menus, leftover directories, Store apps (ICQ, TamTam, VK Play), product directories and local data directories
- **One-click removal** — every detected vector is removed with a dedicated remover; locked databases are reported, never crash
- **Hard search policy** — locks the default search to one of 10 engines (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) via HKLM policies for Chrome, Edge, Brave, Vivaldi and Opera, plus `policies.json` for Firefox/Waterfox
- **Policy cleanup** — strips Mail.ru `DefaultSearchProvider*` values from the registry
- **User data consent** — items containing personal data (Cloud Mail.ru files, ICQ/TamTam history, extensions, cookies, Defender exclusions) are never deleted without explicit confirmation
- **Exclusions** — unchecked findings can be saved and are deselected automatically in future scans
- **Backups** — every registry key and file is exported to `%APPDATA%\AntiVKGroupVanced\backup\` before deletion, plus a full operation log
- **10 UI languages** — ru, en, uk, kk, de, fr, es, pl, tr, zh; system language auto-detected
- **Light UI** — ttkbootstrap, vertical layout, pinned status bar and footer

## Screenshot

<details>
<summary>Main window</summary>

![AntiVKGroupVanced main window](docs/screenshot.png)

</details>

## Ready builds

Download from [Releases](https://github.com/retvil/AntiVKGroupVanced/releases):

- **Windows** — `AntiVKGroupVanced.exe` (portable, single file, ~35 MB) — removes Mail.ru Agent and VK Messenger only
- **Windows** — `AntiVKGroupExtended.exe` (portable, single file, ~35 MB) — removal of every Mail.ru / VK product: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, Store apps, product directories, local data directories, system-wide traces

Both editions are built from the same codebase — pick the one that matches what you have installed. Run it **as administrator** — HKLM policies and registry cleanup require elevated rights.

## Install from source

Requires Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Build your own EXE: run `build.bat` (PyInstaller, output in `dist/`).

## Usage

1. **Kill Processes** → **Search** → **Delete** — remove the apps themselves.
2. **Scan Search Hijacks** — lists every way go.mail.ru hooked into your system.
3. **Remove Hijacks** — close all browsers first, then remove everything found.
4. Pick an engine → **Apply Policy** — your default search is now locked system-wide.
5. **Remove Mail.ru Policies** — strips Mail.ru search policy values if you want to undo step 4.

## FAQ

- **Why administrator?** Default-search policies live in HKLM and hijack cleanup touches system registry — both need elevation.
- **"Database locked" in results?** A Chromium browser was running during cleanup. Close all browsers and run the removal again.
- **How do I undo the search policy?** The **Remove Mail.ru Policies** button strips the policy values; Firefox users can also delete the `distribution\policies.json` file.
- **Why does the app ask for confirmation?** Some findings contain personal data (Cloud Mail.ru files, messenger history, cookies). They are never deleted without your explicit consent.
- **Which edition do I need?** Only Agent / VK Messenger installed → `AntiVKGroupVanced.exe`. Anything else from the Mail.ru / VK family (Cloud, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Author & support

**Nod33Eset** — fork of [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex). Issues and PRs are welcome.

If the tool saved you from Mail.ru, you can support development:

**Crypto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## License

MIT — see [LICENSE](LICENSE).





