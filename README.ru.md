# AntiVKGroup Vanced

[![Release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced?sort=date)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Полностью удаляет ПО Mail.ru и VK из Windows и блокирует поисковый захват через корпоративные политики — 37 векторов обнаружения, 10 языков интерфейса.**

[🇬🇧 English](README.md) | **🇷🇺 Русский**

## Что это?

Mail.ru (VK Group) не просто устанавливает свои приложения — Агент, VK Мессенджер, Облако Mail.ru и поиск go.mail.ru тихо прописывают себя через десятки системных механизмов: ассоциации в реестре, корпоративные политики, настройки профилей браузеров, даже базы поисковых систем внутри профилей Chromium. Простое удаление приложений этого не отменяет.

**AntiVKGroup Vanced** (проект-компаньон [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) находит **все 37 векторов**, удаляет их одним кликом, а затем **жёстко закрепляет поиск по умолчанию** на выбранном вами движке через корпоративные политики Windows — чтобы ничего не могло тихо вернуть захват.

## Возможности

- **Сканер захватов** — обнаруживает 37 векторов: пути установки, записи деинсталляции в реестре, регистрации `StartMenuInternet`, деревья ключей `Software\Mail.Ru`, перехват политики `DefaultSearchProvider*`, `Preferences` профилей Chromium, ключевые слова SQLite в `Web Data`, `search.json.mozlz4` Firefox, устаревшие `SearchScopes`, записи автозагрузки, задачи планировщика, службы Windows, ярлыки, остатки в ProgramData/Roaming, записи hosts, правила брандмауэра, URI-протоколы, расширения браузеров, куки mail.ru, ассоциации «открыть с помощью», следы Prefetch/WER, исключения Defender, перехват Start Page в IE, политики стартовых URL (`RestoreOnStartupURLs`), домашняя страница Firefox, зоновая карта IE, записи RegisteredApplications, следы MUICache, установщики в %TEMP% — плюс, в издании Extended: оверлеи оболочки, контекстные меню, оставшиеся каталоги, приложения Store (ICQ, TamTam, VK Play), каталоги продуктов и локальные каталоги данных
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

**Nod33Eset** — проект-компаньон [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues и PR приветствуются.

Если инструмент избавил вас от Mail.ru, можно поддержать разработку:

**Криптовалюта:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Лицензия

MIT — см. [LICENSE](LICENSE).
