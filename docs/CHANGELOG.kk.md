# Өзгерістер журналы

Бұл жобаның барлық маңызды өзгерістері осы файлда құжатталған.

Формат [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) негізінде
құрылған, жоба [Semantic Versioning](https://semver.org/spec/v2.0.0.html) ұстанады.

## [Шығарылмаған]

## [1.0.0] - 2026-10-22

**AntiVKGroupVanced** — Windows үшін Mail.ru / VK жою құралының алғашқы
релизі, [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)
жобасының серіктесі.

### Қосылды

- Бір кодтан екі нұсқа: **AntiVKGroupVanced** (Mail.ru Агенті және
  VK Мессенджерді жою) және **AntiVKGroupExtended** (барлық Mail.ru / VK
  өнімдері) — `profiles.py` ішіндегі өнім профильдері сканерлеу ауқымын
  таңдайды, ортақ GUI `app.py` ішінде, жұқа кіру нүктелері `main.py` / `main_extended.py`
- **Іздеу басып алу сканері** — Mail.ru / VK бағдарламаларының өзін әдепкі
  іздеу/браузер ретінде орнатуға пайдаланатын 37 векторды анықтайды:
  - істеп тұрған процестер (Агент, VK Мессенджер, Mail.ru Бұлты, ICQ, TamTam,
    VK Play, My.com)
  - дискідегі орнату каталогтары
  - тіркелгідегі жою жазбалары (HKLM, WOW6432Node, HKCU)
  - `StartMenuInternet` браузер клиенттерінің тіркеулері
  - жеке `Software\Mail.Ru` кілттері ағаштары (HKCU/HKLM/WOW6432Node)
  - корпоративтік саясат арқылы басып алу — `DefaultSearchProvider*` тіркелгі мәндері
  - Chromium профильдерінің `Preferences` JSON файлдары (Chrome, Edge, Brave, Vivaldi, Opera)
  - Chromium `Web Data` SQLite дерекқорларындағы іздеу қозғалтқыштарының кілт сөз жолдары
  - Firefox/Waterfox `search.json.mozlz4` (ішінде таза Python жазылған
    LZ4 блок декомпрессорымен)
  - ескірген IE/Windows `SearchScopes` жазбалары
  - автожүктеме жазбалары (`Run`/`RunOnce`)
  - Windows Жоспарлаушы тапсырмалары (Mail.ru жаңарту тапсырмалары)
  - Windows қызметтері (тіркелгі бойынша сканерлеу, `sc stop` + `sc delete` арқылы жою)
  - файл ассоциациялары (`FileExts\<ext>\UserChoice` ішіндегі ProgId сканерлеу + жою)
  - жарлықтар (Жұмыс үстелі / Басты мәзір / тапсырмалар тақтасы)
  - қалдық каталогтар (ProgramData, Roaming)
  - `hosts` жазбалары
  - Windows Firewall ережелері
  - URI хаттама өңдегіштері
  - браузер кеңейтулері (Chromium манифесттері + Firefox `.xpi`)
  - mail.ru кукилері (Chromium + Firefox)
  - `OpenWithProgids`/`OpenWithList` ассоциациялары
  - Prefetch / CrashDumps / WER іздері
  - Windows Defender виняттары
  - IE Start Page басып алуы (`Internet Explorer\Main\Start Page`)
  - старттық URL саясатының басып алуы (Edge, Chrome, Chromium, Brave, Vivaldi, Opera
    ішіндегі `RestoreOnStartupURLs`)
  - Firefox басты бетінің басып алуы (`prefs.js` ішіндегі `browser.startup.homepage`)
  - Mail.ru домендері үшін IE аймақ картасының жазбалары
  - RegisteredApplications жазбалары
  - MUICache ішіндегі іске қосу іздері
  - %TEMP% ішіндегі орнатқыш іздері
  - тек Extended: shell белгі оверлейлері және контекстік мәзір өңдегіштері
  - тек Extended: Store (Appx) қосымшалары — ICQ, TamTam, VK Play және басқа
    Mail.ru / VK Store қосымшалары, `Remove-AppxPackage` арқылы жойылады
  - тек Extended: `Program Files\` астындағы браузерлік емес өнім каталогтары
    (Mail.ru Бұлты, My.com, ...) — жою алдында резервтік көшірме жасалады
  - тек Extended: `%LOCALAPPDATA%\` астындағы браузерлік емес жергілікті деректер
    каталогтары — келісім растауымен, жою алдында резервтік көшірме жасалады
- **Басып алуларды жою** — табылған әр векторды бір рет басумен жою, әр векторға
  арнайы жоюшымен; құлыпталған дерекқорлар/файлдар (браузер істе тұрған) есепте
  көрсетіледі, қателеспейді
- **Қатты әдепкі іздеу саясаты** — 10 іздеу қозғалтқышының бірін бекітеді
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - Chromium тұқымдасы HKLM `SOFTWARE\Policies\...` ішіндегі `DefaultSearchProvider*`
    мәндері арқылы (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox `distribution\policies.json` арқылы
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- **Mail.ru саясаттарын алып тастау** түймесі — Mail.ru `DefaultSearchProvider*`
  саясат мәндерін тіркелгіден алып тастайды
- **Пайдаланушы деректеріне келісім** — жеке деректерге тиетін табылдықтар
  (Mail.ru Бұлты файлдары, ICQ/TamTam тарихы, кеңейтулер, кукилер, Defender
  виняттары) жою алдында нақты қосымша растауды қажет етеді
- Сканерлеуден кейінгі **таңдау диалогы**: «барлығы немесе ештеңе» орнына
  дәл қай табылдықтарды жою керектігін таңдау
- **Виняттар**: таңбаған табылдықтарды `%APPDATA%\AntiVKGroupVanced\exclusions.json`
  ішіне сақтауға болады — болашақ сканерлеулер оларды автоматты түрде алып
  тастайды, бірақ диалогта олар таңдалып қала береді; виняттарды диалогтан
  қайта орнатуға болады
- **Жою алдында резервтік көшірме**: әр тиіп өткен тіркелгі кілті / профиль
  файлы жою алдында `%APPDATA%\AntiVKGroupVanced\backup\<уақыт белгісі>\`
  ішіне экспортталады
- **Операциялар журналы**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 интерфейс тілі** (ru, en, uk, kk, de, fr, es, pl, tr, zh) арнайы
  `translations.py` модулінде; жүйе тілі Windows UI language API арқылы
  (`GetUserDefaultUILanguage`) автоматты анықталады, сәйкестік болмаса — ағылшынша
- ttkbootstrap негізіндегі **жеңіл интерфейс** (`flatly` тақырыбы): тікелей
  терезе орналасуы, орталықтандырылған әрекеттер стегі, толық ені бар секция
  карточкалары, автор, нұсқа және басылмалы GitHub сілтемесі бар бекітілген
  күй жолы мен футер
- Іске қосылғанда әкімші құқықтарын тексеру, күй жолында ескерту
- Басып алуларды жою алдында істеп тұрған браузерді жабу ұсынысы
  («дерекқор құлыпталған» жағдайын болдырмайды)
- Кейбір басып алу элементтерін жою мүмкін болмағанда «есеп папкасын ашу» ұсынысы
- `build.bat` екі нұсқаның EXE файлдарын жинайды (PyInstaller, `--onefile --windowed`)
- Таза логиканың юнит-тесттері: қозғалтқыштарды іздеу, Firefox `policies.json`,
  LZ4 декомпрессоры, `.lnk` байттық анықтау, hosts жолдарын сүзгілеу, firewall
  шығысын талдау, келісім префикстерінің жабылуы, виняттардың сақталуы,
  вектор бойынша жою диспетчері, профиль анықтамалары

[Шығарылмаған]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
