# Registro de cambios

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [No publicado]

## [1.0.0] - 2026-10-22

Lanzamiento inicial de **AntiVKGroupVanced** — una herramienta de eliminación
de Mail.ru / VK para Windows, proyecto compañero de
[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Agregado

- Dos ediciones desde una sola base de código: **AntiVKGroupVanced**
  (eliminación de Mail.ru Agent y VK Messenger) y **AntiVKGroupExtended**
  (todos los productos Mail.ru / VK) — los perfiles de producto en `profiles.py`
  seleccionan el alcance del escaneo, GUI compartida en `app.py`, puntos de
  entrada ligeros `main.py` / `main_extended.py`
- **Escáner de secuestros de búsqueda** — detecta los 37 vectores que el
  software de Mail.ru / VK usa para instalarse como búsqueda/navegador
  predeterminado:
  - procesos en ejecución (Agent, VK Messenger, Cloud Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - directorios de instalación en disco
  - entradas de desinstalación del registro (HKLM, WOW6432Node, HKCU)
  - registros de clientes de navegadores `StartMenuInternet`
  - árboles de claves `Software\Mail.Ru` independientes (HKCU/HKLM/WOW6432Node)
  - secuestro mediante directiva de empresa — valores del registro `DefaultSearchProvider*`
  - JSON `Preferences` de perfiles Chromium (Chrome, Edge, Brave, Vivaldi, Opera)
  - filas de palabras clave de motores de búsqueda en bases de datos SQLite `Web Data` de Chromium
  - `search.json.mozlz4` de Firefox/Waterfox (con un descompresor de bloques LZ4
    en Python puro integrado)
  - entradas heredadas `SearchScopes` de IE/Windows
  - entradas de inicio automático (`Run`/`RunOnce`)
  - entradas del Programador de tareas de Windows (tareas de actualización de Mail.ru)
  - servicios de Windows (escaneo basado en registro, eliminación vía `sc stop` + `sc delete`)
  - asociaciones de archivos (escaneo + eliminación del ProgId en `FileExts\<ext>\UserChoice`)
  - accesos directos (Escritorio / menú Inicio / barra de tareas)
  - directorios residuales (ProgramData, Roaming)
  - entradas `hosts`
  - reglas del Firewall de Windows
  - manejadores de protocolos URI
  - extensiones de navegadores (manifiestos Chromium + `.xpi` de Firefox)
  - cookies de mail.ru (Chromium + Firefox)
  - asociaciones `OpenWithProgids`/`OpenWithList`
  - rastros de Prefetch / CrashDumps / WER
  - exclusiones de Windows Defender
  - secuestro de la página de inicio de IE (`Internet Explorer\Main\Start Page`)
  - secuestro mediante directivas de URL de inicio (`RestoreOnStartupURLs` en
    Edge, Chrome, Chromium, Brave, Vivaldi, Opera)
  - secuestro de la página de inicio de Firefox (`browser.startup.homepage` en `prefs.js`)
  - entradas del mapa de zonas de IE para dominios de Mail.ru
  - entradas RegisteredApplications
  - rastros de ejecución en MUICache
  - rastros de instaladores en %TEMP%
  - solo Extended: superposiciones de iconos de shell y manejadores de menús contextuales
  - solo Extended: aplicaciones de la Store (Appx) — ICQ, TamTam, VK Play y otras
    aplicaciones de Mail.ru / VK de la Store, eliminadas vía `Remove-AppxPackage`
  - solo Extended: directorios de productos no-navegador bajo `Program Files\`
    (Cloud Mail.ru, My.com, ...) con copia de seguridad antes de eliminar
  - solo Extended: directorios de datos locales no-navegador bajo `%LOCALAPPDATA%\`
    — con consentimiento, con copia de seguridad antes de eliminar
- **Eliminación de secuestros** — eliminación con un clic de cada vector
  detectado, con eliminadores dedicados por vector; las bases/archivos
  bloqueados (navegador en ejecución) se informan, nunca se bloquea la aplicación
- **Directiva estricta de buscador predeterminado** — impone uno de los 10
  motores (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant,
  Ecosia, Yahoo, SearXNG):
  - familia Chromium vía valores `DefaultSearchProvider*` en HKLM
    `SOFTWARE\Policies\...` (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox vía `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Botón **Eliminar directivas de Mail.ru** — retira los valores de directiva
  `DefaultSearchProvider*` de Mail.ru del registro
- **Consentimiento para datos personales** — los hallazgos que tocan datos
  personales (archivos de Cloud Mail.ru, historial de ICQ/TamTam, extensiones,
  cookies, exclusiones de Defender) requieren una confirmación adicional
  explícita antes de la eliminación
- **Diálogo de selección** tras el escaneo: elegir exactamente qué hallazgos
  eliminar en lugar de una eliminación todo-o-nada
- **Exclusiones**: los hallazgos desmarcados pueden guardarse en
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — los escaneos futuros los
  desmarcan automáticamente, pero permanecen seleccionables en el diálogo;
  las exclusiones pueden restablecerse desde el diálogo
- **Copia de seguridad antes de eliminar**: cada clave del registro / archivo
  de perfil tocado se exporta a `%APPDATA%\AntiVKGroupVanced\backup\<marca de tiempo>\`
  antes de la eliminación
- **Registro de operaciones**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 idiomas de interfaz** (ru, en, uk, kk, de, fr, es, pl, tr, zh) en un
  módulo dedicado `translations.py`; el idioma del sistema se detecta
  automáticamente mediante la API de idioma de UI de Windows
  (`GetUserDefaultUILanguage`), con inglés como alternativa si no hay coincidencia
- **Interfaz ligera** sobre ttkbootstrap (tema `flatly`): diseño vertical de la
  ventana, pila de acciones centrada, tarjetas de secciones a ancho completo,
  barra de estado y pie de página fijados con autor, versión y enlace de GitHub
  clicable
- Verificación de permisos de administrador al inicio con advertencia en la
  barra de estado
- Aviso para cerrar los navegadores en ejecución antes de eliminar secuestros
  (previene «base de datos bloqueada»)
- Oferta de «Abrir carpeta de informe» cuando algunos elementos de secuestro
  no pudieron eliminarse
- `build.bat` compila los EXE de ambas ediciones (PyInstaller, `--onefile --windowed`)
- Pruebas unitarias de la lógica pura: búsqueda de motores, `policies.json` de
  Firefox, descompresor LZ4, detección de bytes `.lnk`, filtrado de líneas
  hosts, análisis de la salida del firewall, cobertura de prefijos de
  consentimiento, persistencia de exclusiones, despacho de eliminación por
  vector, definiciones de perfiles

[No publicado]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
