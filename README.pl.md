# AntiVKGroup Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  <a href="https://github.com/retvil/AntiWeChatVanced"><img src="https://raw.githubusercontent.com/retvil/AntiWeChatVanced/main/logo.png" alt="AntiWeChatVanced" width="16" height="16" style="vertical-align:middle"> AntiWeChatVanced</a>  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  **AntiVKGroupVanced**  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## Co to jest?

Mail.ru (VK Group) nie tylko instaluje swoje aplikacje — Agent, VK Messenger, Cloud Mail.ru i wyszukiwarka go.mail.ru po cichu rejestrują się przez dziesiątki mechanizmów systemowych: asocjacje w rejestrze, zasady korporacyjne, ustawienia profili przeglądarek, a nawet bazy danych wyszukiwarek wewnątrz profili Chromium. Samo odinstalowanie aplikacji tego nie cofa.

**AntiVKGroup Vanced** (projekt towarzyszący [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) znajduje **wszystkie 37 wektorów**, usuwa je jednym kliknięciem, a następnie **twardo blokuje domyślną wyszukiwarkę** na silniku Twojego wyboru za pomocą zasad korporacyjnych Windows — żeby nic nie mogło jej po cichu odzyskać.

## Funkcje

- **Skaner przejęć** — wykrywa 29 wektorów (VANCED) / 38 wektorów (EXTENDED): ścieżki instalacji, wpisy dezinstalacji w rejestrze, rejestracje `StartMenuInternet`, drzewa kluczy `Software\Mail.Ru`, przejęcie zasad `DefaultSearchProvider*`, `Preferences` profili Chromium, słowa kluczowe SQLite w `Web Data`, `search.json.mozlz4` Firefoksa, przestarzałe `SearchScopes`, wpisy autostartu, zadania harmonogramu, usługi Windows, skróty, pozostałości w ProgramData/Roaming, wpisy hosts, reguły zapory, protokoły URI, rozszerzenia przeglądarek, ciasteczka mail.ru, asocjacje „Otwórz za pomocą", ślady Prefetch/WER, wyjątki Defendera, przejęcie strony startowej IE, zasady adresów startowych (`RestoreOnStartupURLs`), strona główna Firefoksa, mapa stref IE, wpisy RegisteredApplications, ślady MUICache, instalatory w %TEMP% — plus, w edycji Extended: nakładki powłoki, menu kontekstowe, pozostałe katalogi, aplikacje Store (ICQ, TamTam, VK Play), katalogi produktów i katalogi danych lokalnych
- **Usuwanie jednym kliknięciem** — każdy wykryty wektor jest usuwany dedykowanym usuwaczem; zablokowane bazy danych są zgłaszane, nigdy awarii
- **Twarda zasada wyszukiwania** — blokuje domyślną wyszukiwarkę na jednym z 10 silników (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) przez zasady HKLM dla Chrome, Edge, Brave, Vivaldi i Opery, plus `policies.json` dla Firefoksa/Waterfox
- **Czyszczenie zasad** — usuwa wartości `DefaultSearchProvider*` Mail.ru z rejestru
- **Zgoda na dane użytkownika** — elementy zawierające dane osobowe (pliki Cloud Mail.ru, historia ICQ/TamTam, rozszerzenia, ciasteczka, wyjątki Defendera) nigdy nie są usuwane bez wyraźnego potwierdzenia
- **Wyjątki** — odznaczone wyniki można zapisać; w przyszłych skanach są automatycznie odznaczane
- **Kopie zapasowe** — każdy klucz rejestru i plik jest eksportowany do `%APPDATA%\AntiVKGroupVanced\backup\` przed usunięciem, plus pełny dziennik operacji
- **10 języków interfejsu** — ru, en, uk, kk, de, fr, es, pl, tr, zh; język systemu wykrywany automatycznie
- **Lekki interfejs** — ttkbootstrap, układ pionowy, przypięty pasek statusu i stopka

## Zrzut ekranu

<details>
<summary>Okno główne</summary>

![Okno główne AntiVKGroupVanced](docs/screenshot.png)

</details>

## Gotowe buildy

Pobierz ze strony [Releases](https://github.com/retvil/AntiVKGroupVanced/releases):

- **Windows** — `AntiVKGroupVanced.exe` (przenośny, pojedynczy plik, ~35 MB) — usuwa tylko Mail.ru Agent i VK Messenger
- **Windows** — `AntiVKGroupExtended.exe` (przenośny, pojedynczy plik, ~35 MB) — usuwanie wszystkich produktów Mail.ru / VK: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, aplikacje Store, katalogi produktów, katalogi danych lokalnych, ślady systemowe

Obie edycje są budowane z tej samej bazy kodu — wybierz tę, która odpowiada zainstalowanemu oprogramowaniu. Uruchom **jako administrator** — zasady HKLM i czyszczenie rejestru wymagają podwyższonych uprawnień.

## Instalacja ze źródeł

Wymaga Pythona 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Zbuduj własny EXE: uruchom `build.bat` (PyInstaller, wynik w `dist/`).

## Użycie

1. **Zabij procesy** → **Szukaj** → **Usuń** — usunięcie samych aplikacji.
2. **Skanuj przejęcia wyszukiwarki** — pokazuje wszystkie sposoby, jakimi go.mail.ru wszedł do systemu.
3. **Usuń przejęcia** — najpierw zamknij wszystkie przeglądarki, potem usuń wszystko znalezione.
4. Wybierz silnik → **Zastosuj zasadę** — domyślna wyszukiwarka jest teraz zablokowana na poziomie systemu.
5. **Usuń zasady Mail.ru** — usuwa wartości zasad wyszukiwania Mail.ru, jeśli chcesz cofnąć krok 4.

## FAQ

- **Dlaczego administrator?** Zasady domyślnej wyszukiwarki mieszkają w HKLM, a czyszczenie przejęć dotyka rejestru systemowego — oba wymagają podwyższonych uprawnień.
- **„Baza danych zablokowana" w wynikach?** Podczas czyszczenia działała przeglądarka Chromium. Zamknij wszystkie przeglądarki i powtórz usuwanie.
- **Jak cofnąć zasadę wyszukiwania?** Przycisk **Usuń zasady Mail.ru** usuwa wartości zasad; użytkownicy Firefoksa mogą też usunąć plik `distribution\policies.json`.
- **Dlaczego aplikacja prosi o potwierdzenie?** Niektóre wyniki zawierają dane osobowe (pliki Cloud Mail.ru, historia komunikatorów, ciasteczka). Nigdy nie są usuwane bez Twojej wyraźnej zgody.
- **Której edycji potrzebuję?** Zainstalowane tylko Agent / VK Messenger → `AntiVKGroupVanced.exe`. Cokolwiek innego z rodziny Mail.ru / VK (Cloud, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Autor i wsparcie

**Nod33Eset** — projekt towarzyszący [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues i PR mile widziane.

Jeśli narzędzie uratowało Cię przed Mail.ru, możesz wesprzeć rozwój:

**Kryptowaluty:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licencja

MIT — zobacz [LICENSE](LICENSE).


