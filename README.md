# English Vocabulary Learning and Analysis 📚

İngilizce kelime haznesini genişletmek için kelime çalışması uygulaması. Streamlit arayüzü ve CSV tabanlı veri yönetimi kullanır.

---

Linkten siteye ulaşabilirsiniz.
https://english-vocab-learning-chgcipu3jj88u4frdjbiby.streamlit.app

---
## Özellikler

- Rastgele kelime kartları
- Türkçe anlamı tek tıkla gösterme
- "Biliyorum" / "Tekrar Et" akışı
- İlerleme ve durum istatistikleri
- Tek sayfada tüm kelime listesi ve yeni kelime ekleme
- CSV dışa aktarma

---

## Kurulum

### Gereksinimler
- Python 3.9+

### Çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
```

Uygulama tarayıcıda http://localhost:8501 adresinde açılır.

---

## Veri Yapısı

CSV alanları:

| Sütun | Açıklama |
|------|---------|
| English | İngilizce kelime |
| Turkish | Türkçe karşılık |
| Level | Seviye (A1–C1) |
| Status | New / Learning / Mastered |
| Review_Count | Tekrar sayısı |

---

## Kelime Ekleme

### Uygulama içinden
Ana sayfadaki "Kelime Yönetimi" bölümünden yeni kelime ekleyebilirsiniz.

### Dosyadan toplu ekleme
Proje klasörüne extra_words.csv dosyası koyabilirsiniz. Uygulama açılışta bu dosyayı otomatik olarak ekler.

Örnek format:
```
English,Turkish,Level,Status,Review_Count
Example,Örnek,B1,New,0
```

---

## Proje Yapısı

```
english/
├── app.py
├── data_manager.py
├── utils.py
├── requirements.txt
├── english_vocab.csv
├── extra_words.csv
└── README.md
```

---

## Notlar

- İlerleme ve değişiklikler anında CSV dosyasına yazılır.
- Liste büyüdükçe arama/filtreleme eklemek isterseniz kolayca genişletilebilir.

