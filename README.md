# 🤖 Jarvis

Türkçe konuşabilen, sesli komutları anlayabilen ve bilgisayarınızı kontrol edebilen yapay zekâ destekli masaüstü asistanı.

Jarvis; mikrofon üzerinden sizi dinler, konuşmalarınızı yazıya dönüştürür, Groq API ile komutlarınızı analiz eder, gerekli işlemleri gerçekleştirir ve doğal Türkçe ses ile cevap verir.

---

## ✨ Özellikler

* 🎤 Türkçe sesli komut algılama
* 🧠 Groq destekli yapay zekâ karar mekanizması
* 🔊 Edge-TTS ile doğal Türkçe seslendirme
* 🌐 Gerçek zamanlı HUD arayüzü
* 📂 Masaüstünde klasör oluşturma
* 📝 Not alma sistemi
* 📄 Yapay zekâ ile Word belgesi oluşturma
* 🔍 Google aramaları yapabilme
* ▶️ YouTube aramaları açabilme
* 🖥️ Uygulama başlatabilme
* 🔒 Ekran kilitleme desteği

---

## 🛠️ Kullanılan Teknolojiler

* Python
* Faster-Whisper
* Groq API
* Edge-TTS
* NumPy
* SciPy
* SoundDevice
* SoundFile
* Python-Docx

---

## 📦 Kurulum

Depoyu klonlayın:

```bash
git clone https://github.com/yigitefeersoy/jarvis.git
cd jarvis
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

veya

```bash
pip install numpy sounddevice soundfile scipy edge-tts groq faster-whisper python-docx
```

---

## 🔑 Groq API Ayarı

Kod içerisinde bulunan:

```python
GROQ_API_KEY = "API_KEYINIZ"
```

alanını kendi API anahtarınız ile değiştirin.

Groq API anahtarı almak için:

https://groq.com

---

## ▶️ Çalıştırma

```bash
python jarvis.py
```

Başlatıldıktan sonra arayüz otomatik olarak açılır.

Varsayılan adres:

```text
http://127.0.0.1:8777
```

---

## 🗣️ Örnek Komutlar

### Uygulama Açma

* "Not defterini aç"
* "Hesap makinesini aç"
* "YouTube aç"

### Arama Yapma

* "Bugün hava nasıl?"
* "Yapay zekâ nedir?"

### Klasör Oluşturma

* "Masaüstünde proje klasörü oluştur"

### Not Alma

* "Süt almayı not al"

### Yazı Oluşturma

* "Yapay zekâ hakkında yazı yaz"

### Sistem Komutları

* "Saati söyle"
* "Ekranı kilitle"

---

## 📁 Proje Yapısı

```text
jarvis/
│
├── jarvis.py
├── notlar.txt
├── girdi.wav
├── cikti.mp3
├── requirements.txt
└── README.md
```

---

## 📌 Önemli

girdi.wav ile cikti.mp3 dosyaları geçici dosyalardır ve siz jarvis.py ı çalıştırınca otomatik olur girdi sizin sorunuzdur cikti ise cevaptır.

---

## 📌 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz.

1. Fork oluşturun
2. Yeni bir branch açın
3. Değişikliklerinizi yapın
4. Pull Request gönderin

---

## ⭐ Projeyi Destekleyin

Eğer bu proje işinize yaradıysa veya beğendiyseniz:

⭐ GitHub üzerinden projeye yıldız vermeyi unutmayın.

Bir yıldız vermeniz hem projenin daha fazla kişiye ulaşmasına yardımcı olur hem de geliştirme sürecine motivasyon sağlar.

👉 https://github.com/yigitefeersoy/jarvis

"Bir yıldız ücretsizdir, ama geliştirici için oldukça değerlidir." 🚀

Teşekkürler ❤️

---

## 📄 Lisans

Bu proje eğitim, araştırma ve kişisel kullanım amacıyla paylaşılmıştır.
