"""English Vocabulary Learning and Analysis - Ana Uygulama."""

import streamlit as st
from data_manager import DataManager
from utils import (
    get_random_word,
    get_difficulty_emoji,
    get_status_badge,
    get_level_badge
)

# ============================================================================
# SAYFA AYARLARI
# ============================================================================

st.set_page_config(
    page_title="    ",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .flashcard {
        border-radius: 15px;
        padding: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

    .meaning-card {
        border-radius: 15px;
        padding: 40px;
        background: #1d2f4a;
        color: white;
        text-align: center;
        font-size: 48px;
        font-weight: 600;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    
    .stats-container {
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f0f2f6;
    }
    
    .progress-container {
        margin: 20px 0;
    }
    
    .title-main {
        text-align: center;
        color: #667eea;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# OTURUM DURUMU BAŞLATMA
# ============================================================================

if "data" not in st.session_state:
    st.session_state.data = DataManager.load_data()

if "current_word" not in st.session_state:
    st.session_state.current_word = None
    st.session_state.current_meaning = None
    st.session_state.current_level = None
    st.session_state.show_meaning = False

if "last_action" not in st.session_state:
    st.session_state.last_action = None

# ============================================================================
# KENAR PANEL - ANALİZ
# ============================================================================

with st.sidebar:
    st.markdown("### 📊 Analiz Paneli")
    st.divider()
    
    # İstatistikler
    stats = DataManager.get_statistics(st.session_state.data)
    
    # İlerleme çubuğu
    progress = stats["progress_percentage"] / 100
    st.progress(progress)
    
    # Temel metrikler
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Toplam", stats["total_words"])
    with col2:
        st.metric("✅ Ustalaşılan", stats["mastered_count"])
    with col3:
        st.metric("📖 Kalan", stats["total_words"] - stats["mastered_count"])
    
    # Durum dağılımı
    st.markdown("#### Durum Dağılımı")
    status_data = {
        "New": stats["new_count"],
        "Learning": stats["learning_count"],
        "Mastered": stats["mastered_count"]
    }
    status_labels = {
        "New": "Yeni",
        "Learning": "Öğreniliyor",
        "Mastered": "Ustalaşıldı",
    }
    
    for status, count in status_data.items():
        label = status_labels.get(status, status)
        st.write(f"{get_status_badge(status)} {label}: **{count}**")
    
    st.divider()
    
    # En zor kelimeler
    if len(stats["difficult_words"]) > 0:
        st.markdown("#### 🔴 En Zor Kelimeler")
        for idx, row in stats["difficult_words"].iterrows():
            st.write(
                f"{get_difficulty_emoji(row['Review_Count'])} "
                f"**{row['English']}** - {row['Review_Count']} tekrar"
            )
    
    st.divider()
    
    # Ayarlar
    st.markdown("#### ⚙️ Ayarlar")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Yeni Kelime", use_container_width=True):
            st.session_state.current_word = None
            st.session_state.show_meaning = False
            st.rerun()
    
    with col2:
        if st.button("🔴 İlerlemeyi Sıfırla", use_container_width=True):
            st.session_state.data = DataManager.reset_progress()
            st.session_state.current_word = None
            st.session_state.show_meaning = False
            st.success("✅ İlerleme sıfırlandı.")
            st.rerun()
    
    st.divider()
    
    # Alt bilgi
    st.markdown("""
    ---
    **English Vocabulary Learning**
    
    İngilizce kelime çalışmanızı kolaylaştırmak için tasarlanmıştır.
    """)


# ============================================================================
# ANA ALAN
# ============================================================================

# Title
st.markdown("<div class='title-main'>📚 English Vocabulary Learning and Analysis</div>", unsafe_allow_html=True)
st.markdown("**İngilizce kelime öğrenme ve analiz platformu**")
st.divider()

# Kart sistemi
col1, col2, col3 = st.columns([1, 2, 1], gap="large")

with col2:
    # Get or generate current word
    if st.session_state.current_word is None:
        english, meaning, level = get_random_word(st.session_state.data)
        
        if english is not None:
            st.session_state.current_word = english
            st.session_state.current_meaning = meaning
            st.session_state.current_level = level
        else:
            st.success("🎉 Tebrikler! Tüm kelimelerde ustalaştınız.")
            st.balloons()
            st.stop()
    
    # Kartı göster
    st.markdown(f"""
    <div class='flashcard'>
        {st.session_state.current_word}
    </div>
    """, unsafe_allow_html=True)
    
    # Seviye rozeti
    st.markdown(
        f"<div style='text-align: center; margin: 10px 0;'>"
        f"{get_level_badge(st.session_state.current_level)} "
        f"<span style='font-size: 16px;'><b>{st.session_state.current_level}</b></span>"
        f"</div>",
        unsafe_allow_html=True
    )
    
    # Türkçeyi göster/gizle
    if not st.session_state.show_meaning:
        if st.button("👁️ Türkçeyi Göster", use_container_width=True, type="primary"):
            st.session_state.show_meaning = True
            st.rerun()
    else:
        # Display meaning (Turkish only)
        st.markdown(
            f"""
            <div class='meaning-card'>
                {st.session_state.current_meaning}
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # Aksiyon butonları
        action_col1, action_col2 = st.columns(2)
        
        with action_col1:
            if st.button(
                "✅ Biliyorum",
                use_container_width=True,
                type="primary",
                key="know_btn"
            ):
                # Update data
                st.session_state.data = DataManager.mark_as_mastered(
                    st.session_state.data,
                    st.session_state.current_word
                )
                DataManager.save_data(st.session_state.data)
                
                # Reset for next word
                st.session_state.current_word = None
                st.session_state.show_meaning = False
                st.session_state.last_action = "mastered"
                
                st.success("🎉 Harika! Kelime ustalaşıldı.")
                st.rerun()
        
        with action_col2:
            if st.button(
                "❌ Tekrar Et",
                use_container_width=True,
                key="review_btn"
            ):
                # Update data
                st.session_state.data = DataManager.mark_for_review(
                    st.session_state.data,
                    st.session_state.current_word
                )
                DataManager.save_data(st.session_state.data)
                
                # Reset for next word
                st.session_state.current_word = None
                st.session_state.show_meaning = False
                st.session_state.last_action = "review"
                
                st.info("📚 Tekrara alındı. Devam!")
                st.rerun()

st.divider()

# Ek istatistikler
st.markdown("### 📊 Kısa İstatistik")

col1, col2, col3, col4 = st.columns(4)

stats = DataManager.get_statistics(st.session_state.data)

with col1:
    percentage = stats["progress_percentage"]
    st.metric(
        "İlerleme",
        f"{percentage:.1f}%",
        f"{stats['mastered_count']} ustalaşılan"
    )

with col2:
    st.metric(
        "Öğreniliyor",
        stats["learning_count"],
        delta=None
    )

with col3:
    st.metric(
        "Yeni",
        stats["new_count"],
        delta=None
    )

with col4:
    unmastered = stats["total_words"] - stats["mastered_count"]
    st.metric(
        "Kalan",
        unmastered,
        delta=None
    )

# Kelime yönetimi (tek sayfa)
st.markdown("### 🗂️ Kelime Yönetimi")
st.markdown("Yeni kelime ekleyin ve tüm listeyi aşağıda görün.")

with st.form("add_word_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        new_english = st.text_input("İngilizce", placeholder="İngilizce kelime")
    with col2:
        new_turkish = st.text_input("Türkçe", placeholder="Türkçe karşılık")
    with col3:
        new_level = st.selectbox("Seviye", ["A1", "A2", "B1", "B2", "C1"], index=2)

    submit = st.form_submit_button("➕ Kelime Ekle")
    if submit:
        updated = DataManager.add_word(
            st.session_state.data,
            new_english,
            new_turkish,
            new_level,
            "New",
        )
        if len(updated) == len(st.session_state.data):
            st.warning("Bu kelime zaten var veya boş giriş yapıldı.")
        else:
            st.session_state.data = updated
            DataManager.save_data(st.session_state.data)
            st.success("Kelime eklendi.")

# Tam listeyi göster
display_df = st.session_state.data.copy()
display_df["Status"] = display_df["Status"].apply(get_status_badge)
display_df["Level"] = display_df["Level"].apply(get_level_badge)

# Rename columns for display
display_df = display_df.rename(columns={
    "English": "Kelime",
    "Turkish": "Türkçe",
    "Level": "Seviye",
    "Status": "Durum",
    "Review_Count": "Tekrar"
})

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    height=520
)

# İndirme
csv = st.session_state.data.to_csv(index=False)
st.download_button(
    label="📥 CSV İndir",
    data=csv,
    file_name="english_vocab.csv",
    mime="text/csv"
)
