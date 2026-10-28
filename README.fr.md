# AntiVKGroup Vanced

[![Release](https://img.shields.io/github/v/release/retvil/AntiVKGroupVanced?sort=date)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiVKGroupVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Supprime complètement les logiciels Mail.ru et VK de Windows et verrouille votre moteur de recherche par défaut contre le détournement via des stratégies d'entreprise — 37 vecteurs de détection, 10 langues d'interface.**

[🇬🇧 English](README.md) | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | **🇫🇷 Français** | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## Qu'est-ce que c'est ?

Mail.ru (VK Group) ne se contente pas d'installer ses applications — Agent, VK Messenger, Cloud Mail.ru et la recherche go.mail.ru s'enregistrent silencieusement via des dizaines de mécanismes système : associations dans le registre, stratégies d'entreprise, paramètres de profils de navigateurs, voire bases de données de moteurs de recherche à l'intérieur des profils Chromium. Désinstaller les applications ne suffit pas à annuler tout cela.

**AntiVKGroup Vanced** (projet compagnon d'[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) trouve **les 37 vecteurs**, les supprime en un clic, puis **verrouille fermement votre moteur de recherche par défaut** sur le moteur de votre choix via les stratégies d'entreprise de Windows — pour que rien ne puisse le récupérer silencieusement.

## Fonctionnalités

- **Scanner de détournements** — détecte 29 vecteurs (VANCED) / 38 vecteurs (EXTENDED): chemins d'installation, entrées de désinstallation du registre, enregistrements `StartMenuInternet`, arbres de clés `Software\Mail.Ru`, détournement de stratégie `DefaultSearchProvider*`, `Preferences` des profils Chromium, mots-clés SQLite dans `Web Data`, `search.json.mozlz4` de Firefox, `SearchScopes` hérités, entrées de démarrage automatique, tâches planifiées, services Windows, raccourcis, restes dans ProgramData/Roaming, entrées hosts, règles de pare-feu, protocoles URI, extensions de navigateurs, cookies mail.ru, associations « Ouvrir avec », traces Prefetch/WER, exclusions Defender, détournement de la page de démarrage IE, stratégies d'URL de démarrage (`RestoreOnStartupURLs`), page d'accueil Firefox, carte de zones IE, entrées RegisteredApplications, traces MUICache, installateurs dans %TEMP% — plus, dans l'édition Extended : superpositions de shell, menus contextuels, répertoires résiduels, applications Store (ICQ, TamTam, VK Play), répertoires de produits et répertoires de données locales
- **Suppression en un clic** — chaque vecteur détecté est supprimé par un gestionnaire dédié ; les bases de données verrouillées sont signalées, jamais de plantage
- **Stratégie de recherche stricte** — verrouille la recherche par défaut sur l'un des 10 moteurs (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) via des stratégies HKLM pour Chrome, Edge, Brave, Vivaldi et Opera, plus `policies.json` pour Firefox/Waterfox
- **Nettoyage des stratégies** — supprime les valeurs `DefaultSearchProvider*` de Mail.ru du registre
- **Consentement pour les données personnelles** — les éléments contenant des données personnelles (fichiers Cloud Mail.ru, historique ICQ/TamTam, extensions, cookies, exclusions Defender) ne sont jamais supprimés sans confirmation explicite
- **Exclusions** — les résultats décochés peuvent être enregistrés ; ils sont automatiquement désélectionnés lors des scans futurs
- **Sauvegardes** — chaque clé de registre et chaque fichier est exporté vers `%APPDATA%\AntiVKGroupVanced\backup\` avant suppression, plus un journal complet des opérations
- **10 langues d'interface** — ru, en, uk, kk, de, fr, es, pl, tr, zh ; langue du système détectée automatiquement
- **Interface légère** — ttkbootstrap, disposition verticale, barre d'état et pied de page épinglés

## Capture d'écran

<details>
<summary>Fenêtre principale</summary>

![Fenêtre principale d'AntiVKGroupVanced](docs/screenshot.png)

</details>

## Versions prêtes à l'emploi

Téléchargez depuis la page [Releases](https://github.com/retvil/AntiVKGroupVanced/releases) :

- **Windows** — `AntiVKGroupVanced.exe` (portable, fichier unique, ~35 Mo) — supprime uniquement Mail.ru Agent et VK Messenger
- **Windows** — `AntiVKGroupExtended.exe` (portable, fichier unique, ~35 Mo) — suppression de tous les produits Mail.ru / VK : Cloud Mail.ru, ICQ, TamTam, VK Play, My.com, applications Store, répertoires de produits, répertoires de données locales, traces système

Les deux éditions sont compilées à partir de la même base de code — choisissez celle qui correspond à vos logiciels installés. Exécutez **en tant qu'administrateur** — les stratégies HKLM et le nettoyage du registre nécessitent des droits élevés.

## Installation depuis les sources

Nécessite Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiVKGroupVanced.git
cd AntiVKGroupVanced
pip install psutil ttkbootstrap
python main.py
```

Compiler votre propre EXE : lancez `build.bat` (PyInstaller, sortie dans `dist/`).

## Utilisation

1. **Tuer les processus** → **Rechercher** → **Supprimer** — suppression des applications elles-mêmes.
2. **Scanner les détournements de recherche** — liste toutes les façons dont go.mail.ru s'est installé dans votre système.
3. **Supprimer les détournements** — fermez d'abord tous les navigateurs, puis supprimez tout ce qui a été trouvé.
4. Choisissez un moteur → **Appliquer la stratégie** — votre recherche par défaut est désormais verrouillée à l'échelle du système.
5. **Supprimer les stratégies Mail.ru** — retire les valeurs de stratégie de recherche de Mail.ru si vous souhaitez annuler l'étape 4.

## FAQ

- **Pourquoi administrateur ?** Les stratégies de recherche par défaut résident dans HKLM et le nettoyage des détournements touche le registre système — les deux nécessitent des droits élevés.
- **« Base de données verrouillée » dans les résultats ?** Un navigateur Chromium tournait pendant le nettoyage. Fermez tous les navigateurs et relancez la suppression.
- **Comment annuler la stratégie de recherche ?** Le bouton **Supprimer les stratégies Mail.ru** retire les valeurs de stratégie ; les utilisateurs de Firefox peuvent également supprimer le fichier `distribution\policies.json`.
- **Pourquoi l'application demande-t-elle une confirmation ?** Certains résultats contiennent des données personnelles (fichiers Cloud Mail.ru, historique des messageries, cookies). Ils ne sont jamais supprimés sans votre consentement explicite.
- **Quelle édition me faut-il ?** Seuls Agent / VK Messenger installés → `AntiVKGroupVanced.exe`. Autre chose de la famille Mail.ru / VK (Cloud, ICQ, TamTam, VK Play, My.com) → `AntiVKGroupExtended.exe`.

## Auteur et soutien

**Nod33Eset** — projet compagnon d'[AntiYandexVanced](https://github.com/retvil/AntiYandexVanced). Issues et PR bienvenues.

Si l'outil vous a débarrassé de Mail.ru, vous pouvez soutenir le développement :

**Crypto :**

- BTC : `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON : `UQDmvr4SKOxSION3Yky6aOgwAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20) : `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20) : `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL) : `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licence

MIT — voir [LICENSE](LICENSE).

