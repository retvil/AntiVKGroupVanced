# AntiVKGroup Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## ¿Qué es esto?

Mail.ru (VK Group) no solo instala sus aplicaciones — Agent, VK Messenger, Cloud Mail.ru y la búsqueda de go.mail.ru se registran silenciosamente a través de docenas de mecanismos del sistema: asociaciones del registro, directivas de empresa, configuraciones de perfiles de navegadores, incluso bases de datos de motores de búsqueda dentro de los perfiles de Chromium. Desinstalar las aplicaciones por sí solo no deshace todo eso.

**AntiVKGroup Vanced** (proyecto compañero de [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) encuentra **los 37 vectores**, los elimina con un clic y luego **bloquea firmemente tu buscador predeterminado** al motor que elijas mediante directivas de empresa de Windows — para que nada pueda recuperarlo silenciosamente.

## Características

- **Escáner de secuestros** — detecta 29 vectores (VANCED) / 38 vectores (EXTENDED): rutas de instalación, entradas de desinstalación del registro, registros `StartMenuInternet`, árboles de claves `Software\Mail.Ru`, secuestro de directiva `DefaultSearchProvider*`, `Preferences` de perfiles Chromium, palabras clave SQLite en `Web Data`, `search.json.mozlz4` de Firefox, `SearchScopes` heredados, entradas de inicio automático, tareas programadas, servicios de Windows, accesos directos, restos en ProgramData/Roaming, entradas hosts, reglas de firewall, protocolos URI, extensiones de navegadores, cookies de mail.ru, asociaciones «Abrir con», rastros de Prefetch/WER, exclusiones de Defender, secuestro de la página de inicio de IE, directivas de URL de inicio (`RestoreOnStartupURLs`), página de inicio de Firefox, mapa de zonas de IE, entradas RegisteredApplications, rastros de MUICache, instaladores en %TEMP% — más, en la edición Extended: superposiciones de shell, menús contextuales, directorios residuales, aplicaciones de la Store (ICQ, TamTam, VK Play), directorios de productos y directorios de datos locales
- **Eliminación con un clic** — cada vector detectado se elimina con un eliminador dedicado; las bases de datos bloqueadas se informan, nunca se bloquea la aplicación
- **Directiva de búsqueda estricta** — bloquea el buscador predeterminado a uno de los 10 motores (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) mediante directivas HKLM para Chrome, Edge, Brave, Vivaldi y Opera, más `policies.json` para Firefox/Waterfox
- **Limpieza de directivas** — elimina los valores `DefaultSearchProvider*` de Mail.ru del registro
- **Consentimiento para datos personales** — los elementos con datos personales (archivos de Cloud Mail.ru, historial de ICQ/TamTam, extensiones, cookies, exclusiones de Defender) nunca se eliminan sin confirmación explícita
- **Exclusiones** — los hallazgos desmarcados pueden guardarse; en escaneos futuros se desmarcan automáticamente
- **Copias de seguridad** — cada clave del registro y archivo se exporta a `%APPDATA%\AntiVKGroupVanced\backup\` antes de la eliminación, más un registro completo de operaciones
- **10 idiomas de interfaz** — ru, en, uk, kk, de, fr, es, pl, tr, zh; el idioma del sistema se detecta automáticamente
- **Interfaz ligera** — ttkbootstrap, diseño vertical, barra de estado y pie de página fijados

## Captura de pantalla

<details>
<summary>Ventana principal</summary>

![Ventana principal de AntiVKGroupVanced](docs/screenshot.png)

</details>

## Versiones listas

Descarga desde la página de [Releases](https://github.com/retvil/AntiVKGroupVanced/releases):

- **Windows** — `AntiVKGroupVanced.exe` (portable, archivo único, ~35 MB) — elimina solo Mail.ru Agent y VK Messenger
- **Windows** — `AntiVKGroupExtended.exe` (portable, archivo único, ~35 MB) — eliminación de todos los productos Mail.ru / VK: Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, aplicaciones de la Store, directorios de productos, directorios de datos locales, rastros de todo el sistema

Ambas ediciones se compilan desde la misma base de código — elige la que corresponda a tu software instalado. Ejecútalo **como administrador** — las directivas HKLM y la limpieza del registro requieren permisos elevados.

## Instalación desde el código fuente

Requiere Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Compila tu propio EXE: ejecuta `build.bat` (PyInstaller, salida en `dist/`).

## Uso

1. **Matar procesos** → **Buscar** → **Eliminar** — elimina las aplicaciones en sí.
2. **Escanear secuestros de búsqueda** — enumera todas las formas en que go.mail.ru se instaló en tu sistema.
3. **Eliminar secuestros** — cierra primero todos los navegadores, luego elimina todo lo encontrado.
4. Elige un motor → **Aplicar directiva** — tu buscador predeterminado queda bloqueado a nivel del sistema.
5. **Eliminar directivas de Mail.ru** — retira los valores de directiva de búsqueda de Mail.ru si quieres deshacer el paso 4.

## FAQ

- **¿Por qué administrador?** Las directivas del buscador predeterminado residen en HKLM y la limpieza de secuestros toca el registro del sistema — ambas requieren permisos elevados.
- **¿«Base de datos bloqueada» en los resultados?** Un navegador Chromium estaba en ejecución durante la limpieza. Cierra todos los navegadores y repite la eliminación.
- **¿Cómo deshago la directiva de búsqueda?** El botón **Eliminar directivas de Mail.ru** retira los valores de la directiva; los usuarios de Firefox también pueden eliminar el archivo `distribution\policies.json`.
- **¿Por qué la aplicación pide confirmación?** Algunos hallazgos contienen datos personales (archivos de Cloud Mail.ru, historial de mensajería, cookies). Nunca se eliminan sin tu consentimiento explícito.
- **¿Qué edición necesito?** Solo Agent / VK Messenger instalados → `AntiVKGroupVanced.exe`. Algo más de la familia Mail.ru / VK (Cloud, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Autor y apoyo

**Nod33Eset** — proyecto compañero de [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues y PR son bienvenidos.

Si la herramienta te libró de Mail.ru, puedes apoyar el desarrollo:

**Cripto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licencia

MIT — ver [LICENSE](LICENSE).


