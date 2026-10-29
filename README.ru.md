# AntiVKGroup Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  <a href="https://github.com/retvil/AntiWeChatVanced"><img src="https://raw.githubusercontent.com/retvil/AntiWeChatVanced/main/logo.png" alt="AntiWeChatVanced" width="16" height="16" style="vertical-align:middle"> AntiWeChatVanced</a>  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  **AntiVKGroupVanced**  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## Что это?

Mail.ru (VK Group) не просто устанавливает свои приложения — Агент, VK Мессенджер, Облако Mail.ru и поиск go.mail.ru тихо прописывают себя через десятки системных механизмов: ассоциации в реестре, корпоративные политики, настройки профилей браузеров, даже базы поисковых систем внутри профилей Chromium. Простое удаление приложений этого не отменяет.

**AntiVKGroup Vanced** (форк [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) находит **все векторы захвата** (29 в VANCED, 38 в EXTENDED), удаляет их одним кликом, а затем **жёстко закрепляет поиск по умолчанию** на выбранном вами движке через корпоративные политики Windows — чтобы ничего не могло тихо вернуть захват.

## Возможности

- **Сканер захватов** — обнаруживает 29 векторов (VANCED) / 38 векторов (EXTENDED): пути установки, записи деинсталляции в реестре, регистрации `StartMenuInternet`, деревья ключей `Software\Mail.Ru`, перехват политики `DefaultSearchProvider*`, `Preferences` профилей Chromium, ключевые слова SQLite в `Web Data`, `search.json.mozlz4` Firefox, устаревшие `SearchScopes`, записи автозагрузки, задачи планировщика, службы Windows, ярлыки, остатки в ProgramData/Roaming, записи hosts, правила брандмауэра, URI-протоколы, расширения браузеров, куки mail.ru, ассоциации «открыть с помощью», следы Prefetch/WER, исключения Defender, перехват Start Page в IE, политики стартовых URL (`RestoreOnStartupURLs`), домашняя страница Firefox, зоновая карта IE, записи RegisteredApplications, следы MUICache, установщики в %TEMP% — плюс, в издании Extended: оверлеи оболочки, контекстные меню, оставшиеся каталоги, приложения Store (ICQ, TamTam, VK Play), каталоги продуктов и локальные каталоги данных
- **Удаление одним кликом** — каждый найденный вектор удаляется отдельным обработчиком; заблокированные базы данных фиксируются в отчёте, без падений
- **Жёсткая политика поиска** — закрепляет поиск по умолчанию на одном из 10 движков (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) через политики HKLM для Chrome, Edge, Brave, Vivaldi и Opera, плюс `policies.json` для Firefox/Waterfox
- **Очистка политик** — вычищает значения `DefaultSearchProvider*` Mail.ru из реестра
- **Согласие на пользовательские данные** — элементы с личными данными (файлы Облака Mail.ru, история ICQ/TamTam, расширения, куки, исключения Defender) никогда не удаляются без явного подтверждения
- **Исключения** — невыбранные находки можно сохранить; в будущих сканированиях они снимаются автоматически
- **Резервные копии** — каждый ключ реестра и файл экспортируется в `%APPDATA%\AntiVKGroupVanced\backup\` перед удалением, плюс полный журнал операций
- **10 языков интерфейса** — ru, en, uk, kk, de, fr, es, pl, tr, zh; язык системы определяется автоматически
- **Лёгкий интерфейс** — ttkbootstrap, вертикальная компоновка, закреплённые строка статуса и футер

## Скриншот

<details>
<summary>Главное окно</summary>

![Главное окно AntiVKGroupVanced](docs/screenshot.png)

</details>

## Готовые сборки

Скачивайте со страницы [релизов](https://github.com/retvil/AntiVKGroupVanced/releases):

- **Windows** — `AntiVKGroupVanced.exe` (портативный, один файл, ~35 МБ) — удаляет только Агент Mail.ru и VK Мессенджер
- **Windows** — `AntiVKGroupExtended.exe` (портативный, один файл, ~35 МБ) — удаление всех продуктов Mail.ru / VK: Облако Mail.ru, ICQ, TamTam, VK Play, My.com, приложения Store, каталоги продуктов, локальные каталоги данных, общесистемные следы

Оба издания собраны из одной кодовой базы — выбирайте то, что соответствует установленному у вас ПО. Запускайте **от имени администратора** — политики HKLM и очистка реестра требуют повышенных прав.

## Установка из исходников

Требуется Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Собрать свой EXE: запустите `build.bat` (PyInstaller, результат в `dist/`).

## Использование

1. **Завершить процессы** → **Поиск** → **Удалить** — удаление самих приложений.
2. **Сканировать захваты поиска** — показывает все способы, которыми go.mail.ru прописался в системе.
3. **Удалить захваты** — сначала закройте все браузеры, затем удалите всё найденное.
4. Выберите движок → **Применить политику** — поиск по умолчанию закреплён на уровне системы.
5. **Убрать политики Mail.ru** — снимает значения политик поиска Mail.ru, если нужно отменить шаг 4.

## FAQ

- **Зачем права администратора?** Политики поиска по умолчанию живут в HKLM, а очистка захватов трогает системный реестр — и то и другое требует повышения прав.
- **«База данных заблокирована» в результатах?** Во время очистки был запущен Chromium-браузер. Закройте все браузеры и повторите удаление.
- **Как отменить политику поиска?** Кнопка **Убрать политики Mail.ru** вычищает значения политик; пользователи Firefox могут также удалить файл `distribution\policies.json`.
- **Почему приложение просит подтверждение?** Некоторые находки содержат личные данные (файлы Облака Mail.ru, история мессенджеров, куки). Они никогда не удаляются без вашего явного согласия.
- **Какое издание мне нужно?** Установлены только Агент / VK Мессенджер → `AntiVKGroupVanced.exe`. Есть что-то ещё из семейства Mail.ru / VK (Облако, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Автор и поддержка

Изначальная идея: [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex)

Если инструмент избавил вас от Mail.ru, можно поддержать разработку:

**Криптовалюта:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Лицензия

MIT — см. [LICENSE](LICENSE).


