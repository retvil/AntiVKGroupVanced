# AntiVKGroup Vanced

[![Release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced?sort=date)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Windows жүйесінен Mail.ru және VK бағдарламаларын толық жояды және корпоративтік саясаттар арқылы ізді басып алуға қарсы бекітеді — 37 анықтау векторы, 10 интерфейс тілі.**

[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | **🇰🇿 Қазақша** | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## Бұл не?

Mail.ru (VK Group) өз қосымшаларын жай ғана орнатпайды — Агент, VK Мессенджер, Mail.ru Бұлты және go.mail.ru ізі ондаған жүйелік механизм арқылы үнсіз өзін тіркейді: тіркелгідегі ассоциациялар, корпоративтік саясаттар, браузер профильдерінің параметрлері, тіпті Chromium профильдеріндегі іздеу жүйелерінің дерекқорлары. Қосымшаларды жай жою мұның бәрін жоймайды.

**AntiVKGroup Vanced** ([AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) жобасының серіктесі) **барлық 37 векторды** табады, оларды бір рет басумен жояды, содан кейін әдепкі іздеуді сіз таңдаған қозғалтқышқа Windows корпоративтік саясаттары арқылы **қатты бекітеді** — ештеңе оны үнсіз қайта басып ала алмайды.

## Мүмкіндіктер

- **Басып алу сканері** — 37 векторды анықтайды: орнату жолдары, жою тіркелгісі, `StartMenuInternet` тіркеулері, `Software\Mail.Ru` кілттері ағаштары, `DefaultSearchProvider*` саясатын басып алу, Chromium профильдерінің `Preferences` файлдары, `Web Data` SQLite кілт сөздері, Firefox `search.json.mozlz4`, ескірген `SearchScopes`, автожүктеме жазбалары, жоспарлаушы тапсырмалары, Windows қызметтері, жарлықтар, ProgramData/Roaming қалдықтары, hosts жазбалары, firewall ережелері, URI хаттамалары, браузер кеңейтулері, mail.ru кукилері, «арқылы ашу» ассоциациялары, Prefetch/WER іздері, Defender виняттары, IE Start Page басып алуы, старттық URL саясаттары (`RestoreOnStartupURLs`), Firefox басты беті, IE аймақ картасы, RegisteredApplications жазбалары, MUICache іздері, %TEMP% орнатқыштары — сонымен қатар Extended нұсқасында: shell оверлейлері, контекстік мәзірлер, қалдық каталогтар, Store қосымшалары (ICQ, TamTam, VK Play), өнім каталогтары және жергілікті деректер каталогтары
- **Бір рет басумен жою** — әр табылған вектор арнайы жоюшымен жойылады; құлыпталған дерекқорлар есепте көрсетіледі, қателеспейді
- **Қатты іздеу саясаты** — әдепкі іздеуді 10 қозғалтқыштың біріне (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) Chrome, Edge, Brave, Vivaldi және Opera үшін HKLM саясаттары арқылы, Firefox/Waterfox үшін `policies.json` арқылы бекітеді
- **Саясатты тазалау** — Mail.ru `DefaultSearchProvider*` мәндерін тіркелгіден алып тастайды
- **Пайдаланушы деректеріне келісім** — жеке деректер бар элементтер (Mail.ru Бұлты файлдары, ICQ/TamTam тарихы, кеңейтулер, кукилер, Defender виняттары) ешқашан нақты растауменсіз жойылмайды
- **Виняттар** — таңбаған табылдықтарды сақтауға болады; болашақ сканерлеулерде олар автоматты түрде алынады
- **Резервтік көшірмелер** — әр тіркелгі кілті мен файл жою алдында `%APPDATA%\AntiVKGroupVanced\backup\` ішіне экспортталады, сонымен қатар толық операциялар журналы
- **10 интерфейс тілі** — ru, en, uk, kk, de, fr, es, pl, tr, zh; жүйе тілі автоматты анықталады
- **Жеңіл интерфейс** — ttkbootstrap, тікелей орналасу, бекітілген күй жолы және футер

## Скриншот

<details>
<summary>Негізгі терезе</summary>

![AntiVKGroupVanced негізгі терезесі](docs/screenshot.png)

</details>

## Дайын жинақтар

[Релиздер](https://github.com/retvil/AntiVKGroupVanced/releases) бетінен жүктеп алыңыз:

- **Windows** — `AntiVKGroupVanced.exe` (портативті, бір файл, ~35 МБ) — тек Mail.ru Агенті мен VK Мессенджерді жояды
- **Windows** — `AntiVKGroupExtended.exe` (портативті, бір файл, ~35 МБ) — барлық Mail.ru / VK өнімдерін жою: Mail.ru Бұлты, ICQ, TamTam, VK Play, My.com, Store қосымшалары, өнім каталогтары, жергілікті деректер каталогтары, жүйелік іздер

Екі нұсқа да бір кодтан жиналған — орнатылған бағдарламаңызға сәйкесінше таңдаңыз. **Әкімші ретінде** іске қосыңыз — HKLM саясаттары мен тіркелгіні тазалау жоғары құқықтарды қажет етеді.

## Бастапқы кодтан орнату

Python 3.10+ қажет ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Өз EXE жинау: `build.bat` іске қосыңыз (PyInstaller, нәтиже `dist/` ішінде).

## Қолдану

1. **Процестерді өлтіру** → **Іздеу** → **Жою** — қосымшалардың өзін жою.
2. **Іздеу басып ауларын сканерлеу** — go.mail.ru жүйеге қалай енгенін көрсетеді.
3. **Басып алуларды жою** — алдымен барлық браузерді жабыңыз, содан кейін табылғанның бәрін жойыңыз.
4. Қозғалтқышты таңдаңыз → **Саясатты қолдану** — әдепкі іздеу жүйе деңгейінде бекітілді.
5. **Mail.ru саясаттарын алып тастау** — 4-қадамды болдырмау қажет болса, Mail.ru іздеу саясаттарының мәндерін алып тастайды.

## FAQ

- **Неге әкімші құқығы?** Әдепкі іздеу саясаттары HKLM-де тұрады, басып алу тазалауы жүйелік тіркелгіге тиеді — екеуі де жоғары құқықты қажет етеді.
- **Нәтижелерде «Дерекқор құлыпталған»?** Тазалау кезінде Chromium браузері істе тұрған. Барлық браузерді жабып, жоюды қайта орындаңыз.
- **Іздеу саясатын қалай болдырмауға болады?** **Mail.ru саясаттарын алып тастау** түймесі саясат мәндерін алып тастайды; Firefox пайдаланушылары `distribution\policies.json` файлын да жоя алады.
- **Қосымша неге растау сұрайды?** Кейбір табылдықтар жеке деректерді қамтиды (Mail.ru Бұлты файлдары, мессенджер тарихы, кукилер). Олар ешқашан сіздің нақты келісіміңізсіз жойылмайды.
- **Қай нұсқа керек?** Тек Агент / VK Мессенджер орнатылған → `AntiVKGroupVanced.exe`. Mail.ru / VK отбасысынан басқа бірдеңе бар (Бұлт, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Автор және қолдау

**Nod33Eset** — [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) жобасының серіктесі. Issues мен PR қарсы аламыз.

Құрал сізді Mail.ru-дан құтқарса, дамытуды қолдауға болады:

**Криптовалюта:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Лицензия

MIT — қараңыз [LICENSE](LICENSE).

