# Dziennik zmian

Wszystkie istotne zmiany tego projektu są dokumentowane w tym pliku.

Format oparty jest na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
a projekt stosuje [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Nieopublikowane]

## [1.0.0] - 2026-10-22

Pierwsze wydanie **AntiVKGroupVanced** — narzędzia do usuwania Mail.ru / VK
dla Windows, projektu towarzyszącego
[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Dodano

- Dwie edycje z jednej bazy kodu: **AntiVKGroupVanced** (usuwanie Mail.ru
  Agent i VK Messenger) oraz **AntiVKGroupExtended** (wszystkie produkty
  Mail.ru / VK) — profile produktów w `profiles.py` wybierają zakres skanu,
  wspólny GUI w `app.py`, cienkie punkty wejścia `main.py` / `main_extended.py`
- **Skaner przejęć wyszukiwarki** — wykrywa 37 wektorów, którymi oprogramowanie
  Mail.ru / VK instaluje się jako domyślna wyszukiwarka/przeglądarka:
  - uruchomione procesy (Agent, VK Messenger, Cloud Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - katalogi instalacji na dysku
  - wpisy dezinstalacji w rejestrze (HKLM, WOW6432Node, HKCU)
  - rejestracje klientów przeglądarek `StartMenuInternet`
  - samodzielne drzewa kluczy `Software\Mail.Ru` (HKCU/HKLM/WOW6432Node)
  - przejęcie przez zasady korporacyjne — wartości rejestru `DefaultSearchProvider*`
  - JSON `Preferences` profili Chromium (Chrome, Edge, Brave, Vivaldi, Opera)
  - wiersze słów kluczowych wyszukiwarek w bazach SQLite `Web Data` Chromium
  - `search.json.mozlz4` Firefoksa/Waterfox (z wbudowanym dekompresorem bloków
    LZ4 w czystym Pythonie)
  - przestarzałe wpisy `SearchScopes` IE/Windows
  - wpisy autostartu (`Run`/`RunOnce`)
  - wpisy Harmonogramu zadań Windows (zadania aktualizacji Mail.ru)
  - usługi Windows (skan oparty na rejestrze, usuwanie przez `sc stop` + `sc delete`)
  - asocjacje plików (skan + usuwanie ProgId w `FileExts\<ext>\UserChoice`)
  - skróty (Pulpit / menu Start / pasek zadań)
  - pozostałe katalogi (ProgramData, Roaming)
  - wpisy `hosts`
  - reguły Zapory Windows
  - procedury obsługi protokołów URI
  - rozszerzenia przeglądarek (manifesty Chromium + `.xpi` Firefoksa)
  - ciasteczka mail.ru (Chromium + Firefox)
  - asocjacje `OpenWithProgids`/`OpenWithList`
  - ślady Prefetch / CrashDumps / WER
  - wyjątki Windows Defender
  - przejęcie strony startowej IE (`Internet Explorer\Main\Start Page`)
  - przejęcie przez zasady adresów startowych (`RestoreOnStartupURLs` w Edge,
    Chrome, Chromium, Brave, Vivaldi, Opera)
  - przejęcie strony głównej Firefoksa (`browser.startup.homepage` w `prefs.js`)
  - wpisy mapy stref IE dla domen Mail.ru
  - wpisy RegisteredApplications
  - ślady uruchomień w MUICache
  - ślady instalatorów w %TEMP%
  - tylko Extended: nakładki ikon powłoki i procedury obsługi menu kontekstowego
  - tylko Extended: aplikacje Store (Appx) — ICQ, TamTam, VK Play i inne
    aplikacje Mail.ru / VK ze Store, usuwane przez `Remove-AppxPackage`
  - tylko Extended: nieprzeglądarkowe katalogi produktów pod `Program Files\`
    (Cloud Mail.ru, My.com, ...) z kopią zapasową przed usunięciem
  - tylko Extended: nieprzeglądarkowe katalogi danych lokalnych pod `%LOCALAPPDATA%\`
    — z potwierdzeniem zgody, z kopią zapasową przed usunięciem
- **Usuwanie przejęć** — usuwanie każdego wykrytego wektora jednym kliknięciem,
  z dedykowanymi usuwaczami per wektor; zablokowane bazy/pliki (działająca
  przeglądarka) są zgłaszane, nigdy awarii
- **Twarda zasada domyślnej wyszukiwarki** — wymusza jeden z 10 silników
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - rodzina Chromium przez wartości `DefaultSearchProvider*` w HKLM
    `SOFTWARE\Policies\...` (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox przez `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Przycisk **Usuń zasady Mail.ru** — usuwa wartości zasad `DefaultSearchProvider*`
  Mail.ru z rejestru
- **Zgoda na dane użytkownika** — wyniki dotykające danych osobowych (pliki
  Cloud Mail.ru, historia ICQ/TamTam, rozszerzenia, ciasteczka, wyjątki
  Defendera) wymagają wyraźnego dodatkowego potwierdzenia przed usunięciem
- **Dialog wyboru** po skanie: dokładny wybór, które wyniki usunąć, zamiast
  usuwania wszystko-albo-nic
- **Wyjątki**: odznaczone wyniki można zapisać do
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — przyszłe skany automatycznie
  je odznaczają, ale pozostają wybieralne w dialogu; wyjątki można zresetować
  z dialogu
- **Kopia zapasowa przed usunięciem**: każdy dotknięty klucz rejestru / plik
  profilu jest eksportowany do `%APPDATA%\AntiVKGroupVanced\backup\<znacznik czasu>\`
  przed usunięciem
- **Dziennik operacji**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 języków interfejsu** (ru, en, uk, kk, de, fr, es, pl, tr, zh) w dedykowanym
  module `translations.py`; język systemu wykrywany automatycznie przez API
  języka UI Windows (`GetUserDefaultUILanguage`), angielski jako fallback
  przy braku dopasowania
- **Lekki interfejs** na ttkbootstrap (motyw `flatly`): pionowy układ okna,
  wyśrodkowany stos akcji, karty sekcji na pełną szerokość, przypięty pasek
  statusu i stopka z autorem, wersją i klikalnym linkiem do GitHuba
- Sprawdzenie uprawnień administratora przy starcie z ostrzeżeniem w pasku statusu
- Podpowiedź zamknięcia działających przeglądarek przed usuwaniem przejęć
  (zapobiega „baza danych zablokowana")
- Propozycja „otwórz folder raportu", gdy niektórych elementów przejęć nie
  udało się usunąć
- `build.bat` buduje EXE obu edycji (PyInstaller, `--onefile --windowed`)
- Testy jednostkowe czystej logiki: wyszukiwanie silników, `policies.json`
  Firefoksa, dekompresor LZ4, wykrywanie bajtów `.lnk`, filtrowanie linii hosts,
  parsowanie wyjścia zapory, pokrycie prefiksów zgody, trwałość wyjątków,
  dyspozytor usuwania per wektor, definicje profili

[Nieopublikowane]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
