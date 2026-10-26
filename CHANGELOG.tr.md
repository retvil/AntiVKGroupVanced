# Değişiklik günlüğü

Bu projedeki tüm önemli değişiklikler bu dosyada belgelenir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) temel alınarak
hazırlanmıştır ve bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
standardına uyar.

## [Yayınlanmamış]

## [1.0.0] - 2026-10-22

**AntiVKGroupVanced**'ın ilk sürümü — Windows için Mail.ru / VK kaldırma
aracı, [AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)
projesinin kardeşi.

### Eklendi

- Tek kod tabanından iki sürüm: **AntiVKGroupVanced** (Mail.ru Agent ve
  VK Messenger kaldırma) ve **AntiVKGroupExtended** (tüm Mail.ru / VK
  ürünleri) — `profiles.py` içindeki ürün profilleri tarama kapsamını seçer,
  ortak GUI `app.py` içinde, ince giriş noktaları `main.py` / `main_extended.py`
- **Arama ele geçirme tarayıcısı** — Mail.ru / VK yazılımlarının varsayılan
  arama/tarayıcı olarak kendini kurmak için kullandığı 37 vektörü tespit eder:
  - çalışan süreçler (Agent, VK Messenger, Cloud Mail.ru, ICQ, TamTam,
    VK Play, My.com)
  - diskteki kurulum dizinleri
  - kayıt defterindeki kaldırma girdileri (HKLM, WOW6432Node, HKCU)
  - `StartMenuInternet` tarayıcı istemci kayıtları
  - bağımsız `Software\Mail.Ru` anahtar ağaçları (HKCU/HKLM/WOW6432Node)
  - kurumsal ilke üzerinden ele geçirme — `DefaultSearchProvider*` kayıt defteri değerleri
  - profil bazlı Chromium `Preferences` JSON'ları (Chrome, Edge, Brave, Vivaldi, Opera)
  - Chromium `Web Data` SQLite veritabanlarındaki arama motoru anahtar kelime satırları
  - Firefox/Waterfox `search.json.mozlz4` (içinde saf Python ile yazılmış
    LZ4 blok açıcı ile)
  - eski IE/Windows `SearchScopes` girdileri
  - otomatik başlatma girdileri (`Run`/`RunOnce`)
  - Windows Görev Zamanlayıcı girdileri (Mail.ru güncelleyici görevleri)
  - Windows hizmetleri (kayıt defteri tabanlı tarama, `sc stop` + `sc delete` ile kaldırma)
  - dosya ilişkilendirmeleri (`FileExts\<ext>\UserChoice` içinde ProgId taraması + kaldırma)
  - kısayollar (Masaüstü / Başlat menüsü / görev çubuğu)
  - artan dizinler (ProgramData, Roaming)
  - `hosts` girdileri
  - Windows Güvenlik Duvarı kuralları
  - URI protokol işleyicileri
  - tarayıcı uzantıları (Chromium manifestleri + Firefox `.xpi`)
  - mail.ru çerezleri (Chromium + Firefox)
  - `OpenWithProgids`/`OpenWithList` ilişkilendirmeleri
  - Prefetch / CrashDumps / WER izleri
  - Windows Defender istisnaları
  - IE başlangıç sayfası ele geçirmesi (`Internet Explorer\Main\Start Page`)
  - başlangıç URL ilkesi ele geçirmesi (Edge, Chrome, Chromium, Brave, Vivaldi,
    Opera içinde `RestoreOnStartupURLs`)
  - Firefox ana sayfası ele geçirmesi (`prefs.js` içinde `browser.startup.homepage`)
  - Mail.ru alan adları için IE bölge haritası girdileri
  - RegisteredApplications girdileri
  - MUICache içindeki çalıştırma izleri
  - %TEMP% içindeki kurulumcu izleri
  - yalnızca Extended: kabuk simge kaplamaları ve bağlam menüsü işleyicileri
  - yalnızca Extended: Store (Appx) uygulamaları — ICQ, TamTam, VK Play ve diğer
    Mail.ru / VK Store uygulamaları, `Remove-AppxPackage` ile kaldırılır
  - yalnızca Extended: `Program Files\` altındaki tarayıcı dışı ürün dizinleri
    (Cloud Mail.ru, My.com, ...) — silmeden önce yedekleme ile
  - yalnızca Extended: `%LOCALAPPDATA%\` altındaki tarayıcı dışı yerel veri
    dizinleri — onay gerektirir, silmeden önce yedeklenir
- **Ele geçirme kaldırma** — tespit edilen her vektörün tek tıkla kaldırılması,
  vektör başına özel kaldırıcılarla; kilitli veritabanları/dosyalar (tarayıcı
  çalışıyor) raporlanır, asla çökmez
- **Katı varsayılan arama ilkesi** — 10 arama motorundan birini zorunlu kılar
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - Chromium ailesi HKLM `SOFTWARE\Policies\...` içindeki `DefaultSearchProvider*`
    değerleriyle (Chrome, Edge, Brave, Vivaldi, Opera)
  - Firefox/Waterfox `distribution\policies.json` ile
    (`SearchEngines` + `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- **Mail.ru ilkelerini kaldır** düğmesi — Mail.ru `DefaultSearchProvider*`
  ilke değerlerini kayıt defterinden temizler
- **Kullanıcı verisi onayı** — kişisel verilere dokunan bulgular (Cloud Mail.ru
  dosyaları, ICQ/TamTam geçmişi, uzantılar, çerezler, Defender istisnaları)
  kaldırılmadan önce açık ek onay gerektirir
- Taramadan sonra **seçim diyaloğu**: her şeyi-ya da-hiçbir şeyi kaldırmak
  yerine tam olarak hangi bulguların kaldırılacağını seçme
- **İstisnalar**: işaretlenmemiş bulgular `%APPDATA%\AntiVKGroupVanced\exclusions.json`
  içine kaydedilebilir — gelecekteki taramalar bunları otomatik olarak işaretten
  çıkarır, ancak diyaloğda seçilebilir kalırlar; istisnalar diyaloğdan
  sıfırlanabilir
- **Kaldırmadan önce yedekleme**: dokunulan her kayıt defteri anahtarı / profil
  dosyası silmeden önce `%APPDATA%\AntiVKGroupVanced\backup\<zaman damgası>\`
  içine aktarılır
- **İşlem günlüğü**: `%APPDATA%\AntiVKGroupVanced\antivk.log`
- **10 arayüz dili** (ru, en, uk, kk, de, fr, es, pl, tr, zh) özel bir
  `translations.py` modülünde; sistem dili Windows UI language API ile
  (`GetUserDefaultUILanguage`) otomatik algılanır, eşleşme yoksa İngilizce
- ttkbootstrap üzerinde **hafif arayüz** (`flatly` teması): dikey pencere düzeni,
  ortalanmış eylem yığını, tam genişlikte bölüm kartları, yazar, sürüm ve
  tıklanabilir GitHub bağlantısı içeren sabitlenmiş durum çubuğu ve alt bilgi
- Başlangıçta yönetici hakları kontrolü, durum çubuğunda uyarı
- Ele geçirme kaldırmadan önce çalışan tarayıcıları kapatma istemi
  («veritabanı kilitli» durumunu önler)
- Bazı ele geçirme öğeleri kaldırılamadığında «rapor klasörünü aç» önerisi
- `build.bat` her iki sürümün EXE'lerini derler (PyInstaller, `--onefile --windowed`)
- Saf mantık için birim testler: motor arama, Firefox `policies.json`, LZ4
  açıcı, `.lnk` bayt tespiti, hosts satır filtreleme, güvenlik duvarı çıktı
  ayrıştırma, onay öneki kapsamı, istisna kalıcılığı, vektör başına kaldırma
  dağıtıcısı, profil tanımları

[Yayınlanmamış]: https://github.com/retvil/AntiVKGroupVanced/compare/v1.0.0...HEAD
