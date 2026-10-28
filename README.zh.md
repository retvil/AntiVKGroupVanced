# AntiVKGroup Vanced

**🇬🇧 English** | [🇷🇺 Русский](docs/lang_icons/ru.png) | ...

[![Release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced?sort=date)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**彻底清除 Windows 上的 Mail.ru 和 VK 软件，并通过企业策略锁定默认搜索引擎以防劫持 — 37 个检测向量，10 种界面语言。**

[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | **🇨🇳 中文**

## 这是什么？

Mail.ru（VK Group）不只是安装它的应用 — Agent、VK Messenger、Cloud Mail.ru 和 go.mail.ru 搜索会通过数十种系统机制静默注册自己：注册表关联、企业策略、浏览器配置文件设置，甚至 Chromium 配置文件内部的搜索引擎数据库。仅卸载应用并不能撤销这一切。

**AntiVKGroup Vanced**（[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) 的姊妹项目）会找出**全部 37 个向量**，一键清除它们，然后通过 Windows 企业策略**将你的默认搜索引擎牢牢锁定**到你选择的引擎 — 让任何东西都无法静默地把它抢回去。

## 功能

- **劫持扫描器** — 检测 29 个向量 (VANCED) / 38 个向量 (EXTENDED)：安装路径、注册表卸载项、`StartMenuInternet` 注册、独立的 `Software\Mail.Ru` 键树、`DefaultSearchProvider*` 策略劫持、Chromium 配置文件 `Preferences`、`Web Data` SQLite 关键词、Firefox `search.json.mozlz4`、旧式 `SearchScopes`、自启动项、计划任务、Windows 服务、快捷方式、ProgramData/Roaming 残留、hosts 条目、防火墙规则、URI 协议、浏览器扩展、mail.ru Cookie、「打开方式」关联、Prefetch/WER 痕迹、Defender 排除项、IE 起始页劫持、启动 URL 策略（`RestoreOnStartupURLs`）、Firefox 主页、IE 区域映射、RegisteredApplications 条目、MUICache 痕迹、%TEMP% 安装程序 — Extended 版还包括：Shell 图标覆盖、右键菜单、残留目录、Store 应用（ICQ、TamTam、VK Play）、产品目录和本地数据目录
- **一键清除** — 每个检测到的向量都由专用清除器删除；被锁定的数据库会被报告，绝不崩溃
- **严格搜索策略** — 通过 Chrome、Edge、Brave、Vivaldi 和 Opera 的 HKLM 策略，以及 Firefox/Waterfox 的 `policies.json`，将默认搜索锁定到 10 个引擎之一（Google、Bing、DuckDuckGo、Brave Search、Startpage、Mojeek、Qwant、Ecosia、Yahoo、SearXNG）
- **策略清理** — 从注册表中清除 Mail.ru 的 `DefaultSearchProvider*` 值
- **用户数据同意** — 包含个人数据的条目（Cloud Mail.ru 文件、ICQ/TamTam 历史、扩展、Cookie、Defender 排除项）绝不会在没有明确确认的情况下删除
- **排除项** — 未勾选的发现可以保存；在未来的扫描中会自动取消勾选
- **备份** — 删除前，每个注册表键和文件都会导出到 `%APPDATA%\AntiVKGroupVanced\backup\`，外加完整的操作日志
- **10 种界面语言** — ru、en、uk、kk、de、fr、es、pl、tr、zh；自动检测系统语言
- **轻量界面** — ttkbootstrap，垂直布局，固定的状态栏和页脚

## 截图

<details>
<summary>主窗口</summary>

![AntiVKGroupVanced 主窗口](docs/screenshot.png)

</details>

## 现成构建

从 [Releases](https://github.com/retvil/AntiVKGroupVanced/releases) 页面下载：

- **Windows** — `AntiVKGroupVanced.exe`（便携版，单文件，约 35 MB）— 仅删除 Mail.ru Agent 和 VK Messenger
- **Windows** — `AntiVKGroupExtended.exe`（便携版，单文件，约 35 MB）— 删除所有 Mail.ru / VK 产品：Cloud Mail.ru、ICQ、TamTam、VK Play、My.com、Store 应用、产品目录、本地数据目录、全系统痕迹

两个版本都从同一代码库构建 — 根据你安装的软件选择。请**以管理员身份**运行 — HKLM 策略和注册表清理需要提升的权限。

## 从源码安装

需要 Python 3.10+（[python.org](https://python.org)）。

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

构建你自己的 EXE：运行 `build.bat`（PyInstaller，输出在 `dist/`）。

## 使用方法

1. **结束进程** → **搜索** → **删除** — 删除应用本身。
2. **扫描搜索劫持** — 列出 go.mail.ru 进入系统的所有途径。
3. **删除劫持** — 先关闭所有浏览器，然后删除所有发现的内容。
4. 选择一个引擎 → **应用策略** — 你的默认搜索从此在系统范围内被锁定。
5. **删除 Mail.ru 策略** — 如果你想撤销第 4 步，移除 Mail.ru 的搜索策略值。

## 常见问题

- **为什么需要管理员？** 默认搜索策略位于 HKLM，劫持清理会触及系统注册表 — 两者都需要提升的权限。
- **结果中出现「数据库被锁定」？** 清理时有 Chromium 浏览器正在运行。关闭所有浏览器后重新执行删除。
- **如何撤销搜索策略？** **删除 Mail.ru 策略**按钮会移除策略值；Firefox 用户还可以删除 `distribution\policies.json` 文件。
- **为什么应用要求确认？** 某些发现包含个人数据（Cloud Mail.ru 文件、聊天记录、Cookie）。它们绝不会在没有你明确同意的情况下被删除。
- **我需要哪个版本？** 只安装了 Agent / VK Messenger → `AntiVKGroupVanced.exe`。还有其他 Mail.ru / VK 家族软件（Cloud、ICQ、TamTam、VK Play、My.com）→ `AntiVKGroupExtended.exe`。

## 作者与支持

**Nod33Eset** — [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) 的姊妹项目。欢迎提交 Issue 和 PR。

如果这个工具帮你摆脱了 Mail.ru，可以支持开发：

**加密货币：**

- BTC：`bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON：`UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20)：`TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20)：`0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL)：`3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## 许可证

MIT — 见 [LICENSE](LICENSE)。


