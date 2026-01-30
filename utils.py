"""English Vocab Analytics yardımcı fonksiyonları."""

import pandas as pd
from typing import Tuple


def validate_dataframe(df: pd.DataFrame) -> bool:
    """DataFrame yapısını doğrular."""
    required_cols = {"English", "Turkish", "Level", "Status", "Review_Count"}
    return required_cols.issubset(df.columns) and len(df) > 0


def get_random_word(df: pd.DataFrame) -> Tuple[str, str, str]:
    """Ustalaşılmayan kelimelerden rastgele seçer."""
    unmastered = df[df["Status"] != "Mastered"]
    
    if len(unmastered) == 0:
        return None, None, None
    
    random_word = unmastered.sample(n=1).iloc[0]
    return (
        random_word["English"],
        random_word["Turkish"],
        random_word["Level"]
    )


def format_progress_text(mastered: int, total: int) -> str:
    """İlerleme metni oluşturur."""
    return f"{mastered} / {total} words mastered"


def get_difficulty_emoji(review_count: int) -> str:
    """Zorluk seviyesine göre emoji döndürür."""
    if review_count == 0:
        return "🟢"  # Green - new word
    elif review_count <= 2:
        return "🟡"  # Yellow - learning
    elif review_count <= 5:
        return "🟠"  # Orange - difficult
    else:
        return "🔴"  # Red - very difficult


def get_status_badge(status: str) -> str:
    """Durum emojisini döndürür."""
    badges = {
        "New": "🆕",
        "Learning": "📚",
        "Mastered": "✅"
    }
    return badges.get(status, "❓")


def get_level_badge(level: str) -> str:
    """Seviye emojisini döndürür."""
    badges = {
        "B1": "🟦",
        "B2": "🟪",
        "A1": "🟩",
        "A2": "🟨",
        "C1": "🔴",
    }
    return badges.get(level, level)
