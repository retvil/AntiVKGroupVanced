# Журнал змін

Усі значні зміни цього проєкту документуються в цьому файлі.

Формат ґрунтується на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
і проєкт дотримується [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Невипущене]

## [1.0.0] - 2026-10-22

Перший реліз **AntiVKGroupVanced** — інструменту видалення ПЗ Mail.ru / VK для
Windows, проєкту-компаньона [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Додано

- Два видання з однієї кодової бази: **AntiVKGroupVanced** (видалення Агента
  Mail.ru та VK Мессенджера) та **AntiVKGroupExtended** (усі продукти
  Mail.ru / VK) — профілі продуктів у `profiles.py` обирають охоплення
  сканування, спільний GUI в `app.py`, тонкі точки входу `main.py` / `main_extended.py`
- **Сканер пошукових захоплень** — виявляє 37 векторів, якими ПЗ Mail.ru / VK
  прописує себе пошуковиком/браузером за замовчуванням:
  - запущені процеси (Агент, VK Мессенджер, Хмара Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - каталоги встановлення на диску
  - записи видалення в реєстрі (HKLM, WOW6432Node, HKCU)
  - реєстрації клієнтів браузерів `StartMenuInternet`
  - окремі дерева ключів `Software\Mail.Ru` (HKCU/HKLM/WOW6432Node)
  - перехоплення через корпоративні політики — значення реєстру `DefaultSearchProvider*`
  - JSON `Preferences` профілів Chromium (Chrome, Edge, Brave, Vivaldi, Opera)
  - рядки ключових слів пошуковиків у SQLite-базах `Web Data` Chromium
  - `search.json.mozlz4` Firefox/Waterfox (зі вбудованим чисто-Python
    декомпресором LZ4-блоків)
  - застарілі записи `SearchScopes` IE/Windows
  - записи автозавантаження (`Run`/`RunOnce`)
  - завдання Планувальника Windows (завдання оновлення Mail.ru)
  - служби Windows (сканування за реєстром, видалення через `sc stop` + `sc delete`)
  - файлові асоціації (сканування та видалення ProgId у `FileExts\<ext>\UserChoice`)
  - ярлики (Робочий стіл / меню Пуск / панель завдань)
  - залишкові каталоги (ProgramData, Roaming)
  - записи `hosts`
  - правила Брандмауера Windows
  - обробники URI-протоколів
  - розширення браузерів (маніфести Chromium + `.xpi` Firefox)
  - кукі mail.ru (Chromium + Firefox)
  - асоціації `OpenWithProgids`/`OpenWithList`
  - сліди Prefetch / CrashDumps / WER
  - винятки Windows Defender
  - перехоплення Start Page в IE (`Internet Explorer\Main\Start Page`)
  - перехоплення через політики стартових URL (`RestoreOnStartupURLs` в Edge, Chrome,
    Chromium, Brave, Vivaldi, Opera)
  - перехоплення домашньої сторінки Firefox (`browser.startup.homepage` у `prefs.js`)
  - записи зонної карти IE для доменів Mail.ru
  - записи RegisteredApplications
  - сліди запусків у MUICache
  - сліди установників у %TEMP%
  - лише Extended: оверлеї іконок оболонки та обробники контекстного меню
  - лише Extended: застосунки Store (Appx) — ICQ, TamTam, VK Play та інші
    застосунки Mail.ru / VK зі Store, видаляються через `Remove-AppxPackage`
  - лише Extended: небраузерні каталоги продуктів під `Program Files\`
    (Хмара Mail.ru, My.com, ...) з резервним копіюванням перед видаленням
  - лише Extended: небраузерні каталоги локальних даних під `%LOCALAPPDATA%\`
    — з підтвердженням згоди, з резервним копіюванням перед видаленням
- **Видалення захоплень** — видалення кожного знайденого вектора одним кліком
  з окремим обробником для кожного вектора; заблоковані бази/файли
  (запущений браузер) фіксуються у звіті, без падінь
- **Жорстка політика пошуку за замовчуванням** — закріплює один із 10 пошуковиків
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - сімейство Chromium через значення `DefaultSearchProvider*` у HKLM
    `SOFTWARE\Policies\...` (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox через `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Кнопка **Прибрати політики Mail.ru** — вичищає значення політик
  `DefaultSearchProvider*` Mail.ru з реєстру
- **Згода на користувацькі дані** — знахідки, що торкаються особистих
  даних (файли Хмари Mail.ru, історія ICQ/TamTam, розширення, кукі,
  винятки Defender), потребують явного додаткового підтвердження перед видаленням
- **Діалог вибору** після сканування: обрати, які саме знахідки видаляти,
  замість видалення «все або нічого»
- **Винятки**: невибрані знахідки можна зберегти до
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — майбутні сканування знімають
  їх автоматично, але в діалозі вони залишаються доступними; винятки можна
  скинути з діалогу
- **Резервне копіювання перед видаленням**: кожен торкнутий ключ реєстру /
  файл профілю експортується до `%APPDATA%\AntiVKGroupVanced\backup\<мітка часу>\`
  перед видаленням
- **Журнал операцій**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 мов інтерфейсу** (ru, en, uk, kk, de, fr, es, pl, tr, zh) в окремому
  модулі `translations.py`; мова системи визначається автоматично через
  Windows UI language API (`GetUserDefaultUILanguage`), за відсутності
  збігу — англійська
- **Легкий інтерфейс** на ttkbootstrap (тема `flatly`): вертикальна компоновка
  вікна, центрований стек дій, картки секцій на всю ширину, закріплені
  рядок статусу та футер з автором, версією та клікабельним
  посиланням на GitHub
- Перевірка прав адміністратора при запуску з попередженням у рядку статусу
- Пропозиція закрити запущені браузери перед видаленням захоплень
  (запобігає «база даних заблокована»)
- Пропозиція «відкрити папку звіту», якщо деякі елементи захоплень
  не вдалося видалити
- `build.bat` збирає EXE обох видань (PyInstaller, `--onefile --windowed`)
- Юніт-тести чистої логіки: пошук рушіїв, `policies.json` Firefox,
  декомпресор LZ4, побайтове виявлення `.lnk`, фільтрація рядків hosts,
  розбір виводу брандмауера, покриття префіксів згоди, персистентність
  винятків, диспетчер видалення за векторами, визначення профілів

[Невипущене]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
