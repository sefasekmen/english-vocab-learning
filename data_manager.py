"""English Vocabulary Learning and Analysis veri yönetimi."""

import pandas as pd
import os


class DataManager:
    """Kelime verisini yükleme/kaydetme işlemleri."""
    
    CSV_FILE = "english_vocab.csv"
    EXTRA_WORDS_CSV = "extra_words.csv"
    EXTRA_WORDS_TXT = "extra_words.txt"
    
    # B1/B2 örnek akademik kelimeler
    SAMPLE_WORDS = [
        ("Analyze", "Analiz etmek", "B1", "New", 0),
        ("Comprehensive", "Kapsamlı", "B2", "New", 0),
        ("Coherent", "Tutarlı", "B2", "New", 0),
        ("Collaborate", "İşbirliği yapmak", "B1", "New", 0),
        ("Concise", "Özlü", "B2", "New", 0),
        ("Conduct", "Yürütmek", "B1", "New", 0),
        ("Consecutive", "Ardışık", "B2", "New", 0),
        ("Consider", "Dikkate almak", "B1", "New", 0),
        ("Constitute", "Oluşturmak", "B2", "New", 0),
        ("Contribute", "Katkıda bulunmak", "B1", "New", 0),
        ("Crucial", "Çok önemli", "B2", "New", 0),
        ("Debate", "Tartışmak", "B1", "New", 0),
        ("Demonstrate", "Göstermek", "B1", "New", 0),
        ("Derive", "Türetmek", "B2", "New", 0),
        ("Determine", "Belirlemek", "B1", "New", 0),
        ("Develop", "Geliştirmek", "B1", "New", 0),
        ("Devise", "Tasarlamak", "B2", "New", 0),
        ("Disappear", "Kaybolmak", "B1", "New", 0),
        ("Diverse", "Çeşitli", "B2", "New", 0),
        ("Dominate", "Hakim olmak", "B1", "New", 0),
        ("Efficient", "Verimli", "B1", "New", 0),
        ("Enhance", "Geliştirmek", "B2", "New", 0),
        ("Enormous", "Muazzam", "B1", "New", 0),
        ("Ensure", "Sağlamak", "B1", "New", 0),
        ("Establish", "Kurmak", "B1", "New", 0),
        ("Evaluate", "Değerlendirmek", "B1", "New", 0),
        ("Eventually", "Sonunda", "B1", "New", 0),
        ("Evidence", "Kanıt", "B1", "New", 0),
        ("Exceed", "Aşmak", "B2", "New", 0),
        ("Execute", "Uygulamak", "B2", "New", 0),
        ("Exemplify", "Örnek göstermek", "B2", "New", 0),
        ("Exhibit", "Sergilemek", "B2", "New", 0),
        ("Explicit", "Açık", "B2", "New", 0),
        ("Facilitate", "Kolaylaştırmak", "B2", "New", 0),
        ("Feasible", "Uygulanabilir", "B2", "New", 0),
        ("Formulate", "Formüle etmek", "B2", "New", 0),
        ("Fundamental", "Temel", "B1", "New", 0),
        ("Generate", "Üretmek", "B1", "New", 0),
        ("Gradual", "Kademeli", "B1", "New", 0),
        ("Hypothesis", "Hipotez", "B2", "New", 0),
        ("Identical", "Aynı", "B1", "New", 0),
        ("Illustrate", "Göstermek", "B1", "New", 0),
        ("Imply", "İma etmek", "B2", "New", 0),
        ("Implement", "Uygulamak", "B1", "New", 0),
        ("Improve", "İyileştirmek", "B1", "New", 0),
        ("Inadequate", "Yetersiz", "B2", "New", 0),
        ("Incorporate", "Dahil etmek", "B2", "New", 0),
        ("Increase", "Artırmak", "B1", "New", 0),
        ("Inevitable", "Kaçınılmaz", "B2", "New", 0),
        ("Infer", "Sonuç çıkarmak", "B2", "New", 0),
        ("Inherent", "Doğal", "B2", "New", 0),
        ("Maintain", "Sürdürmek", "B1", "New", 0),
        ("Clarify", "Açıklığa kavuşturmak", "B1", "New", 0),
        ("Acquire", "Edinmek", "B1", "New", 0),
        ("Assess", "Değerlendirmek", "B1", "New", 0),
        ("Assume", "Varsaymak", "B2", "New", 0),
        ("Conclude", "Sonuçlandırmak", "B1", "New", 0),
        ("Consequence", "Sonuç", "B1", "New", 0),
        ("Constraint", "Kısıt", "B2", "New", 0),
        ("Context", "Bağlam", "B1", "New", 0),
        ("Contrast", "Karşılaştırmak", "B1", "New", 0),
        ("Criteria", "Kriterler", "B2", "New", 0),
        ("Data", "Veri", "B1", "New", 0),
        ("Decline", "Azalmak", "B1", "New", 0),
        ("Define", "Tanımlamak", "B1", "New", 0),
        ("Distribution", "Dağılım", "B2", "New", 0),
        ("Emphasize", "Vurgulamak", "B1", "New", 0),
        ("Estimation", "Tahmin", "B2", "New", 0),
        ("Exclude", "Hariç tutmak", "B2", "New", 0),
        ("Factor", "Faktör", "B1", "New", 0),
        ("Function", "İşlev", "B1", "New", 0),
        ("Impact", "Etkilemek", "B1", "New", 0),
        ("Indicate", "Belirtmek", "B1", "New", 0),
        ("Interpret", "Yorumlamak", "B2", "New", 0),
        ("Limit", "Sınır", "B1", "New", 0),
        ("Link", "Bağlantı", "B1", "New", 0),
        ("Maintainable", "Sürdürülebilir", "B2", "New", 0),
        ("Method", "Yöntem", "B1", "New", 0),
        ("Occur", "Meydana gelmek", "B1", "New", 0),
        ("Outcome", "Sonuç", "B1", "New", 0),
        ("Principle", "İlke", "B2", "New", 0),
        ("Propose", "Önermek", "B1", "New", 0),
        ("Relevant", "İlgili", "B1", "New", 0),
        ("Reliable", "Güvenilir", "B2", "New", 0),
        ("Require", "Gerektirmek", "B1", "New", 0),
        ("Respond", "Yanıtlamak", "B1", "New", 0),
        ("Significant", "Önemli", "B2", "New", 0),
        ("Similar", "Benzer", "B1", "New", 0),
        ("Source", "Kaynak", "B1", "New", 0),
        ("Structure", "Yapı", "B1", "New", 0),
        ("Sufficient", "Yeterli", "B2", "New", 0),
        ("Survey", "Anket", "B1", "New", 0),
        ("Sustain", "Sürdürmek", "B2", "New", 0),
        ("Trend", "Eğilim", "B1", "New", 0),
        ("Valid", "Geçerli", "B2", "New", 0),
        ("Variable", "Değişken", "B1", "New", 0),
        ("Vision", "Vizyon", "B2", "New", 0),
        ("Voluntary", "Gönüllü", "B2", "New", 0),
        ("Widespread", "Yaygın", "B2", "New", 0),
    ]

    @classmethod
    def _append_external_words(cls, df: pd.DataFrame) -> pd.DataFrame:
        """extra_words.csv veya extra_words.txt varsa listeye ekler."""
        frames = []

        if os.path.exists(cls.EXTRA_WORDS_CSV):
            try:
                extra_df = pd.read_csv(cls.EXTRA_WORDS_CSV)
                if "English" in extra_df.columns:
                    if "Turkish" not in extra_df.columns:
                        extra_df["Turkish"] = ""
                    if "Level" not in extra_df.columns:
                        extra_df["Level"] = "B1"
                    if "Status" not in extra_df.columns:
                        extra_df["Status"] = "New"
                    if "Review_Count" not in extra_df.columns:
                        extra_df["Review_Count"] = 0
                    frames.append(extra_df[["English", "Turkish", "Level", "Status", "Review_Count"]])
            except Exception as e:
                print(f"Error reading {cls.EXTRA_WORDS_CSV}: {e}")

        if os.path.exists(cls.EXTRA_WORDS_TXT):
            try:
                with open(cls.EXTRA_WORDS_TXT, "r", encoding="utf-8") as f:
                    words = [line.strip() for line in f if line.strip()]
                if words:
                    txt_df = pd.DataFrame(
                        {
                            "English": words,
                            "Turkish": [""] * len(words),
                            "Level": ["B1"] * len(words),
                            "Status": ["New"] * len(words),
                            "Review_Count": [0] * len(words),
                        }
                    )
                    frames.append(txt_df)
            except Exception as e:
                print(f"Error reading {cls.EXTRA_WORDS_TXT}: {e}")

        if not frames:
            return df

        extra = pd.concat(frames, ignore_index=True)
        extra["English"] = extra["English"].astype(str).str.strip()
        extra = extra[extra["English"] != ""]
        extra["Turkish"] = extra["Turkish"].fillna("").astype(str)
        extra["Level"] = extra["Level"].fillna("B1").astype(str)
        extra["Status"] = extra["Status"].fillna("New").astype(str)
        extra["Review_Count"] = pd.to_numeric(extra["Review_Count"], errors="coerce").fillna(0).astype(int)

        combined = pd.concat([df, extra], ignore_index=True)
        combined = combined.drop_duplicates(subset=["English"], keep="first")
        return combined
    
    @classmethod
    def initialize_csv(cls) -> pd.DataFrame:
        """CSV yoksa örnek kelimelerle oluşturur."""
        if os.path.exists(cls.CSV_FILE):
            try:
                df = pd.read_csv(cls.CSV_FILE)
                # Validate the dataframe structure
                required_cols = {"English", "Turkish", "Level", "Status", "Review_Count"}
                if not required_cols.issubset(df.columns):
                    raise ValueError("CSV file has invalid columns")
                return df
            except Exception as e:
                print(f"Error reading CSV: {e}. Creating new file.")
        
        # Örnek veri ile yeni CSV oluştur
        df = pd.DataFrame(
            cls.SAMPLE_WORDS,
            columns=["English", "Turkish", "Level", "Status", "Review_Count"]
        )
        df = cls._append_external_words(df)
        df.to_csv(cls.CSV_FILE, index=False)
        return df
    
    @classmethod
    def load_data(cls) -> pd.DataFrame:
        """CSV dosyasından veriyi yükler."""
        if not os.path.exists(cls.CSV_FILE):
            return cls.initialize_csv()
        
        try:
            df = pd.read_csv(cls.CSV_FILE)
            # Veri tiplerini düzelt
            df["Review_Count"] = df["Review_Count"].astype(int)
            updated_df = cls._append_external_words(df)
            if len(updated_df) != len(df):
                cls.save_data(updated_df)
            return updated_df
        except Exception as e:
            print(f"Error loading data: {e}")
            return cls.initialize_csv()
    
    @classmethod
    def save_data(cls, df: pd.DataFrame) -> None:
        """Veriyi CSV dosyasına kaydeder."""
        try:
            df.to_csv(cls.CSV_FILE, index=False)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    @classmethod
    def get_unmastered_words(cls, df: pd.DataFrame) -> pd.DataFrame:
        """Ustalaşılanlar hariç kelimeleri döndürür."""
        return df[df["Status"] != "Mastered"].copy()
    
    @classmethod
    def mark_as_mastered(cls, df: pd.DataFrame, word: str) -> pd.DataFrame:
        """Kelimeyi 'Mastered' olarak işaretler."""
        df.loc[df["English"] == word, "Status"] = "Mastered"
        return df
    
    @classmethod
    def mark_for_review(cls, df: pd.DataFrame, word: str) -> pd.DataFrame:
        """Kelimeyi tekrar listesine alır ve sayacı artırır."""
        mask = df["English"] == word
        df.loc[mask, "Status"] = "Learning"
        df.loc[mask, "Review_Count"] = df.loc[mask, "Review_Count"] + 1
        return df
    
    @classmethod
    def get_statistics(cls, df: pd.DataFrame) -> dict:
        """İstatistikleri hesaplar."""
        total_words = len(df)
        mastered_count = len(df[df["Status"] == "Mastered"])
        learning_count = len(df[df["Status"] == "Learning"])
        new_count = len(df[df["Status"] == "New"])
        
        # En zor kelimeler (en yüksek tekrar sayısı)
        unmastered = df[df["Status"] != "Mastered"]
        difficult_words = (
            unmastered.nlargest(5, "Review_Count")[["English", "Review_Count"]]
            if len(unmastered) > 0
            else pd.DataFrame()
        )
        
        return {
            "total_words": total_words,
            "mastered_count": mastered_count,
            "learning_count": learning_count,
            "new_count": new_count,
            "progress_percentage": (mastered_count / total_words * 100) if total_words > 0 else 0,
            "difficult_words": difficult_words
        }
    
    @classmethod
    def reset_progress(cls) -> pd.DataFrame:
        """Tüm ilerlemeyi sıfırlar."""
        df = cls.load_data()
        df["Status"] = "New"
        df["Review_Count"] = 0
        cls.save_data(df)
        return df

    @classmethod
    def add_word(
        cls,
        df: pd.DataFrame,
        english: str,
        turkish: str,
        level: str = "B1",
        status: str = "New",
    ) -> pd.DataFrame:
        """Yeni kelime ekler (varsa eklemez)."""
        english = (english or "").strip()
        turkish = (turkish or "").strip()
        level = (level or "B1").strip()
        status = (status or "New").strip()

        if not english:
            return df

        if (df["English"].str.lower() == english.lower()).any():
            return df

        new_row = {
            "English": english,
            "Turkish": turkish,
            "Level": level,
            "Status": status,
            "Review_Count": 0,
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        return df
