# AntiVKGroup Vanced

[![Release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced?sort=date)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Повністю видаляє ПЗ Mail.ru та VK з Windows і блокує пошукове захоплення через корпоративні політики — 37 векторів виявлення, 10 мов інтерфейсу.**

[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md) | **🇺🇦 Українська** | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## Що це?

Mail.ru (VK Group) не просто встановлює свої застосунки — Агент, VK Мессенджер, Хмара Mail.ru та пошук go.mail.ru тихо прописуються через десятки системних механізмів: асоціації в реєстрі, корпоративні політики, налаштування профілів браузерів, навіть бази пошукових систем усередині профілів Chromium. Просте видалення застосунків цього не скасовує.

**AntiVKGroup Vanced** (проєкт-компаньон [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) знаходить **усі 37 векторів**, видаляє їх одним кліком, а потім **жорстко закріплює пошук за замовчуванням** на обраному вами рушії через корпоративні політики Windows — щоб ніщо не могло тихо повернути захоплення.

## Можливості

- **Сканер захоплень** — виявляє 37 векторів: шляхи встановлення, записи видалення в реєстрі, реєстрації `StartMenuInternet`, дерева ключів `Software\Mail.Ru`, перехоплення політики `DefaultSearchProvider*`, `Preferences` профілів Chromium, ключові слова SQLite у `Web Data`, `search.json.mozlz4` Firefox, застарілі `SearchScopes`, записи автозавантаження, завдання планувальника, служби Windows, ярлики, залишки в ProgramData/Roaming, записи hosts, правила брандмауера, URI-протоколи, розширення браузерів, кукі mail.ru, асоціації «відкрити за допомогою», сліди Prefetch/WER, винятки Defender, перехват Start Page в IE, політики стартових URL (`RestoreOnStartupURLs`), домашня сторінка Firefox, зонова карта IE, записи RegisteredApplications, сліди MUICache, установники в %TEMP% — плюс, у виданні Extended: оверлеї оболонки, контекстні меню, залишкові каталоги, застосунки Store (ICQ, TamTam, VK Play), каталоги продуктів і локальні каталоги даних
- **Видалення одним кліком** — кожен знайдений вектор видаляється окремим обробником; заблоковані бази даних фіксуються у звіті, без падінь
- **Жорстка політика пошуку** — закріплює пошук за замовчуванням на одному з 10 рушіїв (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) через політики HKLM для Chrome, Edge, Brave, Vivaldi та Opera, плюс `policies.json` для Firefox/Waterfox
- **Очищення політик** — вичищає значення `DefaultSearchProvider*` Mail.ru з реєстру
- **Згода на користувацькі дані** — елементи з особистими даними (файли Хмари Mail.ru, історія ICQ/TamTam, розширення, кукі, винятки Defender) ніколи не видаляються без явного підтвердження
- **Винятки** — невибрані знахідки можна зберегти; у майбутніх скануваннях вони знімаються автоматично
- **Резервні копії** — кожен ключ реєстру та файл експортується до `%APPDATA%\AntiVKGroupVanced\backup\` перед видаленням, плюс повний журнал операцій
- **10 мов інтерфейсу** — ru, en, uk, kk, de, fr, es, pl, tr, zh; мова системи визначається автоматично
- **Легкий інтерфейс** — ttkbootstrap, вертикальна компоновка, закріплені рядок статусу та футер

## Скриншот

<details>
<summary>Головне вікно</summary>

![Головне вікно AntiVKGroupVanced](docs/screenshot.png)

</details>

## Готові збірки

Завантажуйте зі сторінки [релізів](https://github.com/retvil/AntiVKGroupVanced/releases):

- **Windows** — `AntiVKGroupVanced.exe` (портативний, один файл, ~35 МБ) — видаляє лише Агент Mail.ru та VK Мессенджер
- **Windows** — `AntiVKGroupExtended.exe` (портативний, один файл, ~35 МБ) — видалення всіх продуктів Mail.ru / VK: Хмара Mail.ru, ICQ, TamTam, VK Play, My.com, застосунки Store, каталоги продуктів, локальні каталоги даних, загальносистемні сліди

Обидва видання зібрані з однієї кодової бази — обирайте те, що відповідає встановленому у вас ПЗ. Запускайте **від імені адміністратора** — політики HKLM та очищення реєстру потребують підвищених прав.

## Встановлення з вихідників

Потрібен Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Зібрати свій EXE: запустіть `build.bat` (PyInstaller, результат у `dist/`).

## Використання

1. **Завершити процеси** → **Пошук** → **Видалити** — видалення самих застосунків.
2. **Сканувати захоплення пошуку** — показує всі способи, якими go.mail.ru прописався в системі.
3. **Видалити захоплення** — спершу закрийте всі браузери, потім видаліть усе знайдене.
4. Оберіть рушій → **Застосувати політику** — пошук за замовчуванням закріплено на рівні системи.
5. **Прибрати політики Mail.ru** — знімає значення політик пошуку Mail.ru, якщо потрібно скасувати крок 4.

## FAQ

- **Навіщо права адміністратора?** Політики пошуку за замовчуванням живуть в HKLM, а очищення захоплень торкається системного реєстру — і те й інше потребує підвищення прав.
- **«База даних заблокована» у результатах?** Під час очищення був запущений Chromium-браузер. Закрийте всі браузери та повторіть видалення.
- **Як скасувати політику пошуку?** Кнопка **Прибрати політики Mail.ru** вичищає значення політик; користувачі Firefox можуть також видалити файл `distribution\policies.json`.
- **Чому застосунок просить підтвердження?** Деякі знахідки містять особисті дані (файли Хмари Mail.ru, історія месенджерів, кукі). Вони ніколи не видаляються без вашої явної згоди.
- **Яке видання мені потрібне?** Встановлені лише Агент / VK Мессенджер → `AntiVKGroupVanced.exe`. Є щось ще з родини Mail.ru / VK (Хмара, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Автор і підтримка

**Nod33Eset** — проєкт-компаньон [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues та PR вітаються.

Якщо інструмент позбавив вас від Mail.ru, можна підтримати розробку:

**Криптовалюта:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Ліцензія

MIT — див. [LICENSE](LICENSE).

