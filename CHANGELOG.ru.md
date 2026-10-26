# Журнал изменений

Все значимые изменения этого проекта документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
и проект придерживается [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Невышедшее]

## [1.0.0] - 2026-10-22

Первый релиз **AntiVKGroupVanced** — инструмента удаления ПО Mail.ru / VK для
Windows, проекта-компаньона [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Добавлено

- Два издания из одной кодовой базы: **AntiVKGroupVanced** (удаление Агента
  Mail.ru и VK Мессенджера) и **AntiVKGroupExtended** (все продукты
  Mail.ru / VK) — профили продуктов в `profiles.py` выбирают охват сканирования,
  общий GUI в `app.py`, тонкие точки входа `main.py` / `main_extended.py`
- **Сканер поисковых захватов** — обнаруживает 37 векторов, которыми ПО
  Mail.ru / VK прописывает себя поисковиком/браузером по умолчанию:
  - запущенные процессы (Агент, VK Мессенджер, Облако Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - каталоги установки на диске
  - записи деинсталляции в реестре (HKLM, WOW6432Node, HKCU)
  - регистрации клиентов браузеров `StartMenuInternet`
  - отдельные деревья ключей `Software\Mail.Ru` (HKCU/HKLM/WOW6432Node)
  - перехват через корпоративные политики — значения реестра `DefaultSearchProvider*`
  - JSON `Preferences` профилей Chromium (Chrome, Edge, Brave, Vivaldi, Opera)
  - строки ключевых слов поисковиков в SQLite-базах `Web Data` Chromium
  - `search.json.mozlz4` Firefox/Waterfox (со встроенным чисто-Python
    декомпрессором LZ4-блоков)
  - устаревшие записи `SearchScopes` IE/Windows
  - записи автозагрузки (`Run`/`RunOnce`)
  - задачи Планировщика Windows (задачи обновления Mail.ru)
  - службы Windows (сканирование по реестру, удаление через `sc stop` + `sc delete`)
  - файловые ассоциации (сканирование и удаление ProgId в `FileExts\<ext>\UserChoice`)
  - ярлыки (Рабочий стол / меню Пуск / панель задач)
  - оставшиеся каталоги (ProgramData, Roaming)
  - записи `hosts`
  - правила Брандмауэра Windows
  - обработчики URI-протоколов
  - расширения браузеров (манифесты Chromium + `.xpi` Firefox)
  - куки mail.ru (Chromium + Firefox)
  - ассоциации `OpenWithProgids`/`OpenWithList`
  - следы Prefetch / CrashDumps / WER
  - исключения Windows Defender
  - перехват Start Page в IE (`Internet Explorer\Main\Start Page`)
  - перехват через политики стартовых URL (`RestoreOnStartupURLs` в Edge, Chrome,
    Chromium, Brave, Vivaldi, Opera)
  - перехват домашней страницы Firefox (`browser.startup.homepage` в `prefs.js`)
  - записи зонной карты IE для доменов Mail.ru
  - записи RegisteredApplications
  - следы запусков в MUICache
  - следы установщиков в %TEMP%
  - только Extended: оверлеи иконок оболочки и обработчики контекстного меню
  - только Extended: приложения Store (Appx) — ICQ, TamTam, VK Play и другие
    приложения Mail.ru / VK из Store, удаляются через `Remove-AppxPackage`
  - только Extended: небраузерные каталоги продуктов под `Program Files\`
    (Облако Mail.ru, My.com, ...) с резервным копированием перед удалением
  - только Extended: небраузерные каталоги локальных данных под `%LOCALAPPDATA%\`
    — с подтверждением согласия, с резервным копированием перед удалением
- **Удаление захватов** — удаление каждого найденного вектора одним кликом
  с отдельным обработчиком для каждого вектора; заблокированные базы/файлы
  (запущенный браузер) фиксируются в отчёте, без падений
- **Жёсткая политика поиска по умолчанию** — закрепляет один из 10 поисковиков
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - семейство Chromium через значения `DefaultSearchProvider*` в HKLM
    `SOFTWARE\Policies\...` (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox через `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Кнопка **Убрать политики Mail.ru** — вычищает значения политик
  `DefaultSearchProvider*` Mail.ru из реестра
- **Согласие на пользовательские данные** — находки, затрагивающие личные
  данные (файлы Облака Mail.ru, история ICQ/TamTam, расширения, куки,
  исключения Defender), требуют явного дополнительного подтверждения перед удалением
- **Диалог выбора** после сканирования: выбрать, какие именно находки удалять,
  вместо удаления «всё или ничего»
- **Исключения**: невыбранные находки можно сохранить в
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — будущие сканирования снимают
  их автоматически, но в диалоге они остаются доступными; исключения можно
  сбросить из диалога
- **Резервное копирование перед удалением**: каждый затронутый ключ реестра /
  файл профиля экспортируется в `%APPDATA%\AntiVKGroupVanced\backup\<метка времени>\`
  перед удалением
- **Журнал операций**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 языков интерфейса** (ru, en, uk, kk, de, fr, es, pl, tr, zh) в отдельном
  модуле `translations.py`; язык системы определяется автоматически через
  Windows UI language API (`GetUserDefaultUILanguage`), при отсутствии
  совпадения — английский
- **Лёгкий интерфейс** на ttkbootstrap (тема `flatly`): вертикальная компоновка
  окна, центрированный стек действий, карточки секций на всю ширину,
  закреплённые строка статуса и футер с автором, версией и кликабельной
  ссылкой на GitHub
- Проверка прав администратора при запуске с предупреждением в строке статуса
- Предложение закрыть запущенные браузеры перед удалением захватов
  (предотвращает «база данных заблокирована»)
- Предложение «открыть папку отчёта», если некоторые элементы захватов
  не удалось удалить
- `build.bat` собирает EXE обоих изданий (PyInstaller, `--onefile --windowed`)
- Юнит-тесты чистой логики: поиск движков, `policies.json` Firefox,
  декомпрессор LZ4, побайтовое обнаружение `.lnk`, фильтрация строк hosts,
  разбор вывода брандмауэра, покрытие префиксов согласия, персистентность
  исключений, диспетчер удаления по векторам, определения профилей

[Невышедшее]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
