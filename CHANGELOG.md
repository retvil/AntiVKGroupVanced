# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-10-22

### Added

- Initial release of AntiVKGroupVanced — Mail.ru / VK removal tool for Windows.
- Two editions: **AntiVKGroupVanced** (Mail.ru Agent + VK Messenger) and **AntiVKGroupExtended** (all Mail.ru / VK products: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, Store apps, product and local data directories).
- Deep scan across processes, registry uninstall entries, install directories, browser hijacks (go.mail.ru), scheduled tasks, services, shortcuts, startup entries, hosts file, firewall rules, Defender exclusions, Store apps, shell overlays, context menus.
- Search hijack removal with per-vector selection and browser-close confirmation.
- Default search engine enforcement via Chromium enterprise policies and Firefox policies.json; removal of Mail.ru search policies.
- Mandatory user consent for items containing personal data (Cloud Mail.ru files, ICQ/TamTam history, extensions, cookies, antivirus exclusions).
- Selection dialog with persistent user exclusions (`%APPDATA%\AntiVKGroupVanced\exclusions.json`).
- Automatic backups of every registry key and file before deletion (`%APPDATA%\AntiVKGroupVanced\backup\`) plus operation log (`antivk.log`).
- GUI in 10 languages: Russian, English, Ukrainian, Kazakh, German, French, Spanish, Polish, Turkish, Chinese.
- PyInstaller build script producing both edition EXEs.
