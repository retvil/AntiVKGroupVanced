# Journal des modifications

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Non publié]

## [1.0.0] - 2026-10-22

Première version de **AntiVKGroupVanced** — un outil de suppression Mail.ru / VK
pour Windows, projet compagnon d'[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced).

### Ajouté

- Deux éditions à partir d'une seule base de code : **AntiVKGroupVanced**
  (suppression de Mail.ru Agent et VK Messenger) et **AntiVKGroupExtended**
  (tous les produits Mail.ru / VK) — les profils de produits dans `profiles.py`
  sélectionnent le périmètre de scan, GUI partagé dans `app.py`, points d'entrée
  minces `main.py` / `main_extended.py`
- **Scanner de détournements de recherche** — détecte les 37 vecteurs utilisés
  par les logiciels Mail.ru / VK pour s'installer comme recherche/navigateur
  par défaut :
  - processus en cours d'exécution (Agent, VK Messenger, Cloud Mail.ru, ICQ,
    TamTam, VK Play, My.com)
  - répertoires d'installation sur le disque
  - entrées de désinstallation du registre (HKLM, WOW6432Node, HKCU)
  - enregistrements de clients de navigateurs `StartMenuInternet`
  - arbres de clés `Software\Mail.Ru` autonomes (HKCU/HKLM/WOW6432Node)
  - détournement via stratégie d'entreprise — valeurs de registre `DefaultSearchProvider*`
  - JSON `Preferences` des profils Chromium (Chrome, Edge, Brave, Vivaldi, Opera)
  - lignes de mots-clés de moteurs de recherche dans les bases SQLite `Web Data` de Chromium
  - `search.json.mozlz4` de Firefox/Waterfox (avec un décompresseur de blocs LZ4
    en pur Python intégré)
  - entrées `SearchScopes` héritées d'IE/Windows
  - entrées de démarrage automatique (`Run`/`RunOnce`)
  - entrées du Planificateur de tâches Windows (tâches de mise à jour Mail.ru)
  - services Windows (scan basé sur le registre, suppression via `sc stop` + `sc delete`)
  - associations de fichiers (scan + suppression du ProgId dans `FileExts\<ext>\UserChoice`)
  - raccourcis (Bureau / menu Démarrer / barre des tâches)
  - répertoires résiduels (ProgramData, Roaming)
  - entrées `hosts`
  - règles du Pare-feu Windows
  - gestionnaires de protocoles URI
  - extensions de navigateurs (manifestes Chromium + `.xpi` Firefox)
  - cookies mail.ru (Chromium + Firefox)
  - associations `OpenWithProgids`/`OpenWithList`
  - traces Prefetch / CrashDumps / WER
  - exclusions Windows Defender
  - détournement de la page de démarrage IE (`Internet Explorer\Main\Start Page`)
  - détournement via stratégies d'URL de démarrage (`RestoreOnStartupURLs` dans
    Edge, Chrome, Chromium, Brave, Vivaldi, Opera)
  - détournement de la page d'accueil Firefox (`browser.startup.homepage` dans `prefs.js`)
  - entrées de la carte de zones IE pour les domaines Mail.ru
  - entrées RegisteredApplications
  - traces d'exécution MUICache
  - traces d'installateurs dans %TEMP%
  - Extended uniquement : superpositions d'icônes de shell et gestionnaires de menus contextuels
  - Extended uniquement : applications Store (Appx) — ICQ, TamTam, VK Play et
    autres applications Mail.ru / VK du Store, supprimées via `Remove-AppxPackage`
  - Extended uniquement : répertoires de produits non-navigateur sous `Program Files\`
    (Cloud Mail.ru, My.com, ...) avec sauvegarde avant suppression
  - Extended uniquement : répertoires de données locales non-navigateur sous
    `%LOCALAPPDATA%\` — soumis à consentement, sauvegardés avant suppression
- **Suppression des détournements** — suppression en un clic de chaque vecteur
  détecté, avec des gestionnaires dédiés par vecteur ; les bases/fichiers
  verrouillés (navigateur en cours) sont signalés, jamais de plantage
- **Stratégie stricte de recherche par défaut** — impose l'un des 10 moteurs
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG) :
  - famille Chromium via les valeurs `DefaultSearchProvider*` dans HKLM
    `SOFTWARE\Policies\...` (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox via `distribution\policies.json`
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Bouton **Supprimer les stratégies Mail.ru** — retire les valeurs de stratégie
  `DefaultSearchProvider*` de Mail.ru du registre
- **Consentement pour les données personnelles** — les résultats touchant des
  données personnelles (fichiers Cloud Mail.ru, historique ICQ/TamTam,
  extensions, cookies, exclusions Defender) exigent une confirmation
  supplémentaire explicite avant suppression
- **Dialogue de sélection** après le scan : choisir exactement quels résultats
  supprimer au lieu d'une suppression tout-ou-rien
- **Exclusions** : les résultats décochés peuvent être enregistrés dans
  `%APPDATA%\AntiVKGroupVanced\exclusions.json` — les scans futurs les
  désélectionnent automatiquement, mais ils restent sélectionnables dans le
  dialogue ; les exclusions peuvent être réinitialisées depuis le dialogue
- **Sauvegarde avant suppression** : chaque clé de registre / fichier de profil
  touché est exporté vers `%APPDATA%\AntiVKGroupVanced\backup\<horodatage>\`
  avant suppression
- **Journal des opérations** : `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 langues d'interface** (ru, en, uk, kk, de, fr, es, pl, tr, zh) dans un
  module dédié `translations.py` ; langue du système détectée automatiquement
  via l'API de langue UI Windows (`GetUserDefaultUILanguage`), repli sur
  l'anglais en l'absence de correspondance
- **Interface légère** sur ttkbootstrap (thème `flatly`) : disposition verticale
  de la fenêtre, pile d'actions centrée, cartes de sections pleine largeur,
  barre d'état et pied de page épinglés avec auteur, version et lien GitHub
  cliquable
- Vérification des droits administrateur au démarrage avec avertissement dans
  la barre d'état
- Invite à fermer les navigateurs en cours avant la suppression des
  détournements (évite « base de données verrouillée »)
- Proposition « Ouvrir le dossier du rapport » lorsque certains éléments de
  détournement n'ont pas pu être supprimés
- `build.bat` compile les EXE des deux éditions (PyInstaller, `--onefile --windowed`)
- Tests unitaires de la logique pure : recherche de moteurs, `policies.json`
  Firefox, décompresseur LZ4, détection d'octets `.lnk`, filtrage des lignes
  hosts, analyse de la sortie du pare-feu, couverture des préfixes de
  consentement, persistance des exclusions, dispatch de suppression par
  vecteur, définitions de profils

[Non publié]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
