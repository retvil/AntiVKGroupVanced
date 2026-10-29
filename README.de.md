# AntiVKGroup Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  <a href="https://github.com/retvil/AntiWeChatVanced"><img src="https://raw.githubusercontent.com/retvil/AntiWeChatVanced/main/logo.png" alt="AntiWeChatVanced" width="16" height="16" style="vertical-align:middle"> AntiWeChatVanced</a>  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  **AntiVKGroupVanced**  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## Was ist das?

Mail.ru (VK Group) installiert nicht nur seine Apps — Agent, VK Messenger, Cloud Mail.ru und die go.mail.ru-Suche tragen sich still über Dutzende Systemmechanismen ein: Registrierungsassoziationen, Unternehmensrichtlinien, profileigene Browsereinstellungen, sogar Suchmaschinen-Datenbanken innerhalb von Chromium-Profilen. Alleiniges Deinstallieren der Apps macht das nicht rückgängig.

**AntiVKGroup Vanced** (ein Schwesterprojekt von [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) findet **alle 37 Vektoren**, entfernt sie mit einem Klick und **sperrt dann Ihre Standardsuche** hart auf eine Engine Ihrer Wahl über Windows-Unternehmensrichtlinien — damit nichts sie sich still zurückholen kann.

## Funktionen

- **Hijack-Scanner** — erkennt 29 Vektoren (VANCED) / 38 Vektoren (EXTENDED): Installationspfade, Deinstallations-Registrierungseinträge, `StartMenuInternet`-Registrierungen, `Software\Mail.Ru`-Schlüsselbäume, `DefaultSearchProvider*`-Richtlinien-Hijack, Chromium-Profil-`Preferences`, `Web Data`-SQLite-Schlüsselwörter, Firefox `search.json.mozlz4`, veraltete `SearchScopes`, Autostart-Einträge, Aufgabenplaner-Aufgaben, Windows-Dienste, Verknüpfungen, ProgramData/Roaming-Reste, hosts-Einträge, Firewall-Regeln, URI-Protokolle, Browser-Erweiterungen, mail.ru-Cookies, „Öffnen mit"-Zuordnungen, Prefetch/WER-Spuren, Defender-Ausschlüsse, IE-Startseiten-Hijack, Start-URL-Richtlinien (`RestoreOnStartupURLs`), Firefox-Startseite, IE-Zonenzuordnung, RegisteredApplications-Einträge, MUICache-Spuren, %TEMP%-Installer — plus in der Extended-Edition: Shell-Overlays, Kontextmenüs, übrig gebliebene Verzeichnisse, Store-Apps (ICQ, TamTam, VK Play), Produktverzeichnisse und lokale Datenverzeichnisse
- **Ein-Klick-Entfernung** — jeder gefundene Vektor wird mit einem eigenen Entferner entfernt; gesperrte Datenbanken werden gemeldet, nie Abstürze
- **Harte Suchrichtlinie** — sperrt die Standardsuche auf eine von 10 Engines (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) über HKLM-Richtlinien für Chrome, Edge, Brave, Vivaldi und Opera, plus `policies.json` für Firefox/Waterfox
- **Richtlinien-Bereinigung** — entfernt Mail.ru-`DefaultSearchProvider*`-Werte aus der Registrierung
- **Nutzerdaten-Zustimmung** — Elemente mit persönlichen Daten (Cloud-Mail.ru-Dateien, ICQ/TamTam-Verlauf, Erweiterungen, Cookies, Defender-Ausschlüsse) werden nie ohne ausdrückliche Bestätigung gelöscht
- **Ausschlüsse** — abgewählte Funde können gespeichert werden; künftige Scans wählen sie automatisch ab
- **Backups** — jeder Registrierungsschlüssel und jede Datei wird vor dem Löschen nach `%APPDATA%\AntiVKGroupVanced\backup\` exportiert, plus vollständiges Operationsprotokoll
- **10 UI-Sprachen** — ru, en, uk, kk, de, fr, es, pl, tr, zh; Systemsprache wird automatisch erkannt
- **Leichtes UI** — ttkbootstrap, vertikales Layout, fixierte Statusleiste und Fußzeile

## Screenshot

<details>
<summary>Hauptfenster</summary>

![AntiVKGroupVanced Hauptfenster](docs/screenshot.png)

</details>

## Fertige Builds

Download von der [Releases](https://github.com/retvil/AntiVKGroupVanced/releases)-Seite:

- **Windows** — `AntiVKGroupVanced.exe` (portabel, Einzeldatei, ~35 MB) — entfernt nur Mail.ru Agent und VK Messenger
- **Windows** — `AntiVKGroupExtended.exe` (portabel, Einzeldatei, ~35 MB) — Entfernung jedes Mail.ru-/VK-Produkts: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, Store-Apps, Produktverzeichnisse, lokale Datenverzeichnisse, systemweite Spuren

Beide Editionen stammen aus derselben Codebasis — wählen Sie diejenige, die zu Ihrer installierten Software passt. Als **Administrator ausführen** — HKLM-Richtlinien und Registrierungsbereinigung erfordern erhöhte Rechte.

## Installation aus dem Quellcode

Erfordert Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Eigenes EXE bauen: `build.bat` ausführen (PyInstaller, Ausgabe in `dist/`).

## Verwendung

1. **Prozesse beenden** → **Suchen** → **Löschen** — die Apps selbst entfernen.
2. **Such-Hijacks scannen** — listet jede Art auf, wie sich go.mail.ru ins System eingetragen hat.
3. **Hijacks entfernen** — zuerst alle Browser schließen, dann alles Gefundene entfernen.
4. Engine wählen → **Richtlinie anwenden** — Ihre Standardsuche ist jetzt systemweit gesperrt.
5. **Mail.ru-Richtlinien entfernen** — entfernt die Suchrichtlinien-Werte von Mail.ru, wenn Sie Schritt 4 rückgängig machen wollen.

## FAQ

- **Warum Administrator?** Richtlinien für die Standardsuche liegen in HKLM und die Hijack-Bereinigung berührt die Systemregistrierung — beides erfordert erhöhte Rechte.
- **„Datenbank gesperrt" in den Ergebnissen?** Während der Bereinigung lief ein Chromium-Browser. Alle Browser schließen und die Entfernung wiederholen.
- **Wie mache ich die Suchrichtlinie rückgängig?** Der Button **Mail.ru-Richtlinien entfernen** entfernt die Richtlinienwerte; Firefox-Nutzer können zusätzlich die Datei `distribution\policies.json` löschen.
- **Warum fragt die App nach Bestätigung?** Einige Funde enthalten persönliche Daten (Cloud-Mail.ru-Dateien, Messenger-Verlauf, Cookies). Sie werden nie ohne Ihre ausdrückliche Zustimmung gelöscht.
- **Welche Edition brauche ich?** Nur Agent / VK Messenger installiert → `AntiVKGroupVanced.exe`. Sonstiges aus der Mail.ru-/VK-Familie (Cloud, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Autor & Unterstützung

**Nod33Eset** — Schwesterprojekt von [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues und PRs sind willkommen.

Wenn das Tool Sie von Mail.ru befreit hat, können Sie die Entwicklung unterstützen:

**Krypto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Lizenz

MIT — siehe [LICENSE](LICENSE).


