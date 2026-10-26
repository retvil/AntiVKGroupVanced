# 更新日志

本项目的所有重要变更都记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，
本项目遵循 [Semantic Versioning](https://semver.org/spec/v2.0.0.html)。

## [未发布]

## [1.0.0] - 2026-10-22

**AntiVKGroupVanced** 首个版本 — Windows 上的 Mail.ru / VK 清除工具，
[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) 的姊妹项目。

### 新增

- 单一代码库的两个版本：**AntiVKGroupVanced**（删除 Mail.ru Agent 和
  VK Messenger）与 **AntiVKGroupExtended**（所有 Mail.ru / VK 产品）—
  `profiles.py` 中的产品配置选择扫描范围，共享 GUI 位于 `app.py`，
  轻量入口 `main.py` / `main_extended.py`
- **搜索劫持扫描器** — 检测 Mail.ru / VK 软件用来把自己安装为默认搜索/浏览器的
  全部 37 个向量：
  - 正在运行的进程（Agent、VK Messenger、Cloud Mail.ru、ICQ、TamTam、
    VK Play、My.com）
  - 磁盘上的安装目录
  - 注册表卸载项（HKLM、WOW6432Node、HKCU）
  - `StartMenuInternet` 浏览器客户端注册
  - 独立的 `Software\Mail.Ru` 键树（HKCU/HKLM/WOW6432Node）
  - 企业策略劫持 — `DefaultSearchProvider*` 注册表值
  - 按配置文件的 Chromium `Preferences` JSON（Chrome、Edge、Brave、Vivaldi、Opera）
  - Chromium `Web Data` SQLite 数据库中的搜索引擎关键词行
  - Firefox/Waterfox `search.json.mozlz4`（内置纯 Python 实现的 LZ4 块解压器）
  - 旧式 IE/Windows `SearchScopes` 条目
  - 自启动项（`Run`/`RunOnce`）
  - Windows 任务计划程序条目（Mail.ru 更新任务）
  - Windows 服务（基于注册表的扫描，通过 `sc stop` + `sc delete` 删除）
  - 文件关联（扫描 + 删除 `FileExts\<ext>\UserChoice` 中的 ProgId）
  - 快捷方式（桌面 / 开始菜单 / 任务栏）
  - 残留目录（ProgramData、Roaming）
  - `hosts` 条目
  - Windows 防火墙规则
  - URI 协议处理器
  - 浏览器扩展（Chromium manifest + Firefox `.xpi`）
  - mail.ru Cookie（Chromium + Firefox）
  - `OpenWithProgids`/`OpenWithList` 关联
  - Prefetch / CrashDumps / WER 痕迹
  - Windows Defender 排除项
  - IE 起始页劫持（`Internet Explorer\Main\Start Page`）
  - 启动 URL 策略劫持（Edge、Chrome、Chromium、Brave、Vivaldi、Opera 中的
    `RestoreOnStartupURLs`）
  - Firefox 主页劫持（`prefs.js` 中的 `browser.startup.homepage`）
  - 针对 Mail.ru 域名的 IE 区域映射条目
  - RegisteredApplications 条目
  - MUICache 中的运行痕迹
  - %TEMP% 中的安装程序痕迹
  - 仅 Extended：Shell 图标覆盖和右键菜单处理器
  - 仅 Extended：Store（Appx）应用 — ICQ、TamTam、VK Play 及其他 Mail.ru / VK
    Store 应用，通过 `Remove-AppxPackage` 删除
  - 仅 Extended：`Program Files\` 下的非浏览器产品目录（Cloud Mail.ru、
    My.com 等）— 删除前备份
  - 仅 Extended：`%LOCALAPPDATA%\` 下的非浏览器本地数据目录 — 需要同意，
    删除前备份
- **劫持清除** — 一键清除每个检测到的向量，每个向量配有专用清除器；
  被锁定的数据库/文件（浏览器正在运行）会被报告，绝不崩溃
- **严格默认搜索策略** — 强制使用 10 个引擎之一（Google、Bing、DuckDuckGo、
  Brave Search、Startpage、Mojeek、Qwant、Ecosia、Yahoo、SearXNG）：
  - Chromium 家族通过 HKLM `SOFTWARE\Policies\...` 中的 `DefaultSearchProvider*`
    值（Chrome、Edge、Brave、Vivaldi、Opera）
  - Firefox/Waterfox 通过 `distribution\policies.json`
    （`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`）
- **删除 Mail.ru 策略**按钮 — 从注册表中清除 Mail.ru 的 `DefaultSearchProvider*`
  策略值
- **用户数据同意** — 涉及个人数据的发现（Cloud Mail.ru 文件、ICQ/TamTam 历史、
  扩展、Cookie、Defender 排除项）在删除前需要明确的额外确认
- 扫描后的**选择对话框**：精确选择要删除哪些发现，而不是全删或不删
- **排除项**：未勾选的发现可以保存到 `%APPDATA%\AntiVKGroupVanced\exclusions.json`
  — 未来的扫描会自动取消勾选它们，但在对话框中仍可选择；排除项可以从对话框重置
- **删除前备份**：每个被触及的注册表键 / 配置文件在删除前都会导出到
  `%APPDATA%\AntiVKGroupVanced\backup\<时间戳>\`
- **操作日志**：`%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 种界面语言**（ru、en、uk、kk、de、fr、es、pl、tr、zh），位于专用的
  `translations.py` 模块；通过 Windows UI language API
  （`GetUserDefaultUILanguage`）自动检测系统语言，无匹配时回退到英语
- 基于 ttkbootstrap 的**轻量界面**（`flatly` 主题）：垂直窗口布局、居中的
  操作堆栈、全宽分区卡片、固定的状态栏和页脚（含作者、版本和可点击的
  GitHub 链接）
- 启动时检查管理员权限，并在状态栏显示警告
- 清除劫持前提示关闭正在运行的浏览器（防止「数据库被锁定」）
- 当部分劫持条目无法删除时，提供「打开报告文件夹」选项
- `build.bat` 构建两个版本的 EXE（PyInstaller，`--onefile --windowed`）
- 纯逻辑的单元测试：引擎查找、Firefox `policies.json`、LZ4 解压器、`.lnk`
  字节检测、hosts 行过滤、防火墙输出解析、同意前缀覆盖、排除项持久化、
  按向量的删除分发、产品配置定义

[未发布]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
