# Änderungsprotokoll

Alle wesentlichen Änderungen dieses Projekts werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unveröffentlicht]

## [1.0.0] - 2026-10-22

Erstveröffentlichung von **AntiVKGroupVanced** — einem Mail.ru-/VK-Entfernungs-
Tool für Windows, einem Schwesterprojekt von
[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Hinzugefügt

- Zwei Editionen aus einer Codebasis: **AntiVKGroupVanced** (Entfernung von
  Mail.ru Agent und VK Messenger) und **AntiVKGroupExtended** (jedes
  Mail.ru-/VK-Produkt) — Produktprofile in `profiles.py` wählen den
  Scan-Umfang, gemeinsame GUI in `app.py`, schlanke Einstiegspunkte
  `main.py` / `main_extended.py`
- **Such-Hijack-Scanner** — erkennt 37 Vektoren, mit denen sich Mail.ru-/VK-
  Software als Standardsuche/Browser einträgt:
  - laufende Prozesse (Agent, VK Messenger, Cloud Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - Installationsverzeichnisse auf der Festplatte
  - Deinstallations-Registrierungseinträge (HKLM, WOW6432Node, HKCU)
  - `StartMenuInternet`-Browserclient-Registrierungen
  - eigenständige `Software\Mail.Ru`-Schlüsselbäume (HKCU/HKLM/WOW6432Node)
  - Richtlinien-Hijack über `DefaultSearchProvider*`-Registrierungswerte
  - profilbezogene Chromium-`Preferences`-JSONs (Chrome, Edge, Brave, Vivaldi, Opera)
  - Suchmaschinen-Schlüsselwortzeilen in Chromium-`Web Data`-SQLite-Datenbanken
  - Firefox/Waterfox `search.json.mozlz4` (mit eingebautem reinem Python-
    LZ4-Block-Dekompressor)
  - veraltete IE/Windows-`SearchScopes`-Einträge
  - Autostart-Einträge (`Run`/`RunOnce`)
  - Windows-Aufgabenplaner-Einträge (Mail.ru-Updater-Aufgaben)
  - Windows-Dienste (registrierungsbasierte Suche, Entfernung via `sc stop` + `sc delete`)
  - Dateizuordnungen (ProgId-Scan + Entfernung in `FileExts\<ext>\UserChoice`)
  - Verknüpfungen (Desktop / Startmenü / Taskleiste)
  - übrig gebliebene Verzeichnisse (ProgramData, Roaming)
  - `hosts`-Einträge
  - Windows-Firewall-Regeln
  - URI-Protokoll-Handler
  - Browser-Erweiterungen (Chromium-Manifeste + Firefox-`.xpi`)
  - mail.ru-Cookies (Chromium + Firefox)
  - `OpenWithProgids`/`OpenWithList`-Zuordnungen
  - Prefetch-/CrashDumps-/WER-Spuren
  - Windows-Defender-Ausschlüsse
  - IE-Startseiten-Hijack (`Internet Explorer\Main\Start Page`)
  - Start-URL-Richtlinien-Hijack (`RestoreOnStartupURLs` in Edge, Chrome,
    Chromium, Brave, Vivaldi, Opera)
  - Firefox-Startseiten-Hijack (`browser.startup.homepage` in `prefs.js`)
  - IE-Zonenzuordnungs-Einträge für Mail.ru-Domänen
  - RegisteredApplications-Einträge
  - MUICache-Ausführungsspuren
  - %TEMP%-Installer-Spuren
  - nur Extended: Shell-Symbol-Overlays und Kontextmenü-Handler
  - nur Extended: Store-Apps (Appx) — ICQ, TamTam, VK Play und andere
    Mail.ru-/VK-Store-Apps, entfernt via `Remove-AppxPackage`
  - nur Extended: Nicht-Browser-Produktverzeichnisse unter `Program Files\`
    (Cloud Mail.ru, My.com, ...) mit Backup-vor-Löschung
  - nur Extended: Nicht-Browser-lokale Datenverzeichnisse unter `%LOCALAPPDATA%\`
    — zustimmungspflichtig, mit Backup vor der Löschung
- **Hijack-Entfernung** — Ein-Klick-Entfernung jedes gefundenen Vektors mit
  Vektor-eigenen Entfernern; gesperrte Datenbanken/Dateien (Browser läuft)
  werden gemeldet, nie Abstürze
- **Harte Standardsuch-Richtlinie** — erzwingt eine von 10 Suchmaschinen
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - Chromium-Familie via HKLM `SOFTWARE\Policies\...` `DefaultSearchProvider*`-
    Werte (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox via `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Button **Mail.ru-Richtlinien entfernen** — entfernt Mail.ru-
  `DefaultSearchProvider*`-Richtlinienwerte aus der Registrierung
- **Nutzerdaten-Zustimmung** — Funde, die persönliche Daten berühren
  (Cloud-Mail.ru-Dateien, ICQ/TamTam-Verlauf, Erweiterungen, Cookies,
  Defender-Ausschlüsse), erfordern vor der Entfernung eine ausdrückliche
  zusätzliche Bestätigung
- **Auswahldialog** nach dem Scan: genau auswählen, welche Funde entfernt
  werden sollen, statt Alles-oder-Nichts-Entfernung
- **Ausschlüsse**: abgewählte Funde können in
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` gespeichert werden — künftige
  Scans wählen sie automatisch ab, sie bleiben aber im Dialog auswählbar;
  Ausschlüsse können aus dem Dialog zurückgesetzt werden
- **Backup vor der Entfernung**: jeder berührte Registrierungsschlüssel /
  jede Profildatei wird vor dem Löschen nach
  `%APPDATA%\AntiVKGroupVanced\backup\<Zeitstempel>\` exportiert
- **Operationsprotokoll**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 UI-Sprachen** (ru, en, uk, kk, de, fr, es, pl, tr, zh) in einem eigenen
  `translations.py`-Modul; Systemsprache wird automatisch über die Windows-UI-
  Sprach-API erkannt (`GetUserDefaultUILanguage`), Englisch als Fallback
- **Leichtes UI** auf ttkbootstrap (`flatly`-Theme): vertikales Fensterlayout,
  zentrierter Aktionsstapel, Sektionskarten in voller Breite, fixierte
  Statusleiste und Fußzeile mit Autor, Version und klickbarem GitHub-Link
- Administratorrechte-Prüfung beim Start mit Warnung in der Statusleiste
- Aufforderung, laufende Browser vor der Hijack-Entfernung zu schließen
  (verhindert „Datenbank gesperrt")
- Angebot „Berichtordner öffnen", wenn einige Hijack-Elemente nicht entfernt
  werden konnten
- `build.bat` baut die EXEs beider Editionen (PyInstaller, `--onefile --windowed`)
- Unit-Tests für reine Logik: Engine-Suche, Firefox `policies.json`,
  LZ4-Dekompressor, `.lnk`-Byte-Erkennung, hosts-Zeilenfilterung, Firewall-
  Ausgabeparsing, Zustimmungspräfix-Abdeckung, Ausschluss-Persistenz,
  Entfernungs-Dispatch pro Vektor, Profildefinitionen

[Unveröffentlicht]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
