# AntiVKGroupVanced

> Removes Mail.ru and VK software from Windows: Agent, VK Messenger, Cloud Mail.ru, go.mail.ru search hijacks, ICQ, TamTam, VK Play, My.com — and everything they leave behind.

[![GitHub release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced)](https://github.com/retvil/AntiVKGroupVanced/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Language / Язык:** [English](#features) | [Русский](#antivkgroupvanced-1)

## Features

- **Deep scan** of processes, registry, files, browser hijacks, scheduled tasks, services, shortcuts, startup entries, hosts file, firewall rules, Defender exclusions, Store apps and more.
- **Two editions**:
  - **AntiVKGroupVanced** — Mail.ru Agent + VK Messenger only (lightweight).
  - **AntiVKGroupExtended** — everything: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, Store apps, product directories, local data directories, shell overlays, context menus, hosts, firewall, Defender exclusions.
- **Search hijack removal** — restores browser settings hijacked to go.mail.ru across Chromium browsers and Firefox.
- **Default search policy** — enforce your preferred search engine via enterprise policies (survives re-hijacks), or remove Mail.ru policies.
- **User data consent** — items containing personal data (Cloud Mail.ru files, ICQ/TamTam history, extensions, cookies, antivirus exclusions) are never deleted without explicit confirmation.
- **Selection dialog** — review every finding before removal; unchecked items can be added to exclusions and will be deselected automatically in future scans.
- **Backups** — every registry key and file is exported to `%APPDATA%\AntiVKGroupVanced\backup\` before deletion, plus a full operation log.
- **10 UI languages** — Russian, English, Ukrainian, Kazakh, German, French, Spanish, Polish, Turkish, Chinese.

## Quick Start

### Download (recommended)

Grab a ready EXE from the [Releases](https://github.com/retvil/AntiVKGroupVanced/releases) page:

- `AntiVKGroupVanced.exe` — Agent + VK Messenger
- `AntiVKGroupExtended.exe` — all Mail.ru / VK products

Run it, click **Search**, review the findings, click **Delete**.

### Build from source

Requirements: Windows 10+, Python 3.10+.

```bat
build.bat
```

Both EXE files appear in the `dist\` folder.

## Configuration

No configuration required. Optional:

- **Exclusions** — persisted in `%APPDATA%\AntiVKGroupVanced\exclusions.json`.
- **Operation log** — `%APPDATA%\AntiVKGroupVanced\antivk.log`.
- **Backups** — `%APPDATA%\AntiVKGroupVanced\backup\<timestamp>\`.

## Architecture

Single codebase, two entry points:

| File | Purpose |
|---|---|
| `main.py` / `main_extended.py` | Entry points (Vanced / Extended) |
| `app.py` | Tkinter GUI and workflow orchestration |
| `profiles.py` | Scan step definitions per edition |
| `mailru_detect.py` | Detection and removal engine |
| `products_detect.py` | Product directories, Store apps, local data |
| `engines.py` | Search engine definitions |
| `policies.py` | Chromium/Firefox enterprise policies |
| `backup.py` | Registry/file backups and operation log |
| `exclusions.py` | Persistent user exclusions |
| `translations.py` | UI translations (10 languages) |

## Development

```bat
python -m pytest tests\ -q
```

## Donations

If this tool saved you time, consider supporting the project:

- **BTC**: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- **TON**: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- **USDT TRC20**: `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- **USDT ERC20**: `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- **USDT SOL**: `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## License

MIT — see [LICENSE](LICENSE).

---

# AntiVKGroupVanced

> Удаляет ПО Mail.ru и VK из Windows: Агент, VK Мессенджер, Облако Mail.ru, поисковые захваты go.mail.ru, ICQ, TamTam, VK Play, My.com — и всё, что они оставляют после себя.

## Возможности

- **Глубокое сканирование** процессов, реестра, файлов, захватов браузеров, планировщика задач, служб, ярлыков, автозагрузки, hosts, правил брандмауэра, исключений Defender, приложений Store и многого другого.
- **Два издания**:
  - **AntiVKGroupVanced** — только Агент + VK Мессенджер (лёгкое).
  - **AntiVKGroupExtended** — всё: Облако Mail.ru, ICQ, TamTam, VK Play, My.com, приложения Store, каталоги продуктов, локальные каталоги данных, оверлеи оболочки, контекстные меню, hosts, брандмауэр, исключения Defender.
- **Удаление поисковых захватов** — восстанавливает настройки браузеров, захваченные на go.mail.ru, в Chromium-браузерах и Firefox.
- **Политика поиска по умолчанию** — закрепляет выбранный поисковик через корпоративные политики (переживает повторные захваты) или снимает политики Mail.ru.
- **Согласие на пользовательские данные** — элементы с личными данными (файлы Облака Mail.ru, история ICQ/TamTam, расширения, куки, исключения антивируса) не удаляются без явного подтверждения.
- **Диалог выбора** — просмотр всех находок перед удалением; невыбранные элементы можно добавить в исключения — в будущих сканированиях они снимаются автоматически.
- **Резервные копии** — каждый ключ реестра и файл экспортируется в `%APPDATA%\AntiVKGroupVanced\backup\` перед удалением, плюс полный журнал операций.
- **10 языков интерфейса** — русский, английский, украинский, казахский, немецкий, французский, испанский, польский, турецкий, китайский.

## Быстрый старт

### Скачивание (рекомендуется)

Готовые EXE на странице [релизов](https://github.com/retvil/AntiVKGroupVanced/releases):

- `AntiVKGroupVanced.exe` — Агент + VK Мессенджер
- `AntiVKGroupExtended.exe` — все продукты Mail.ru / VK

Запустите, нажмите **Поиск**, просмотрите находки, нажмите **Удалить**.

### Сборка из исходников

Требования: Windows 10+, Python 3.10+.

```bat
build.bat
```

Оба EXE появятся в папке `dist\`.

## Настройка

Настройка не требуется. Опционально:

- **Исключения** — хранятся в `%APPDATA%\AntiVKGroupVanced\exclusions.json`.
- **Журнал операций** — `%APPDATA%\AntiVKGroupVanced\antivk.log`.
- **Резервные копии** — `%APPDATA%\AntiVKGroupVanced\backup\<метка времени>\`.

## Разработка

```bat
python -m pytest tests\ -q
```

## Поддержать проект

Если инструмент сэкономил вам время, поддержите разработку:

- **BTC**: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- **TON**: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- **USDT TRC20**: `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- **USDT ERC20**: `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- **USDT SOL**: `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Лицензия

MIT — см. [LICENSE](LICENSE).
