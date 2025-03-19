import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

COLOR_MAP = {
    "POSITIVE": "#90EE90",
    "NEGATIVE": "#FF6B6B",
    "NEUTRAL": "#FFD93D"
}

EMOJI_MAP = {
    "POSITIVE": "😊",
    "NEGATIVE": "😠",
    "NEUTRAL": "😐"
}

st.set_page_config(page_title="Duygu Analizi", layout="wide")
st.title("🎨 Dinamik Renkli Duygu Analizi")

# Yan panel
with st.sidebar:
    st.header("⚙️ Ayarlar")
    st.markdown("""
    **Kullanılan Model:**  
    `cardiffnlp/twitter-roberta-base-sentiment`  
    (3 sınıflı Twitter duygu analiz modeli)
    
    **Renk Kodlaması:**
    - 🟢 Pozitif: #90EE90 (Açık Yeşil)
    - 🔴 Negatif: #FF6B6B (Açık Kırmızı)
    - 🟡 Nötr: #FFD93D (Açık Sarı)
    """)
    
    st.header("ℹ️ Bilgi Paneli")
    st.markdown("""
    **Uygulama Özellikleri:**
    - Metin girişine göre gerçek zamanlı duygu analizi
    - Duyguya özel dinamik arka plan rengi
    - Duygu etiketi ve güven skoru görüntüleme
    - Renk geçiş animasyonu
    """)

user_input = st.text_input("Metni girin:", "")

if user_input:
    classifier = load_model()
    result = classifier(user_input)[0]
    
    # Etiket dönüşümü
    label_num = int(result['label'].split("_")[-1])
    label = ["NEGATIVE", "NEUTRAL", "POSITIVE"][label_num]
    
    # CSS injection
    st.markdown(
        f"""
        <style>
            [data-testid="stAppViewContainer"] > .main {{
                background-color: {COLOR_MAP[label]};
                transition: background-color 0.5s ease;
            }}
            [data-testid="stHeader"] {{
                background-color: rgba(0,0,0,0);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{EMOJI_MAP[label]} Sonuç: {label}")
    with col2:
        st.metric("Güven Skoru", f"{result['score']:.2%}")

else:
    st.info("Lütfen bir metin giriniz")

def show_help_section():
    st.sidebar.subheader("📖 Yardım ve Bilgiler")
    
    # Temel yardım bilgileri
    st.sidebar.markdown("""
    **Güven Skoru:**  
    Modelin tahminine olan güveni 0-1 arasında (yüksek = daha emin)
    
    **Hızlı Kılavuz:**  
    - 😊 Pozitif Duygu  
    - 😠 Negatif Duygu  
    - 😐 Nötr Duygu  
    - Renkler duyguya göre otomatik değişir
    """)
    
    # Detaylı bilgiler için expander
    with st.sidebar.expander("📊 Detaylı Teknik Bilgiler"):
        st.markdown("""
        **Güven Skoru (Confidence Score)**
        - **Hesaplama Yöntemi:** Model çıktılarından direkt alınır (`result['score']`)
        - **Yorumlama:**  
          0.0-0.4 → Düşük güven  
          0.4-0.6 → Orta güven  
          0.6-1.0 → Yüksek güven

        **Renk Kodları**  
        | Duygu   | HEX Kodu   | Örnek      |
        |---------|------------|------------|
        | Pozitif | `#90EE90`  | 🟩 Açık Yeşil |
        | Negatif | `#FF6B6B`  | 🟥 Açık Kırmızı |
        | Nötr    | `#FFD93D`  | 🟨 Açık Sarı |

        **Emoji Sembolojisi**  
        - 😊 → Olumlu kelimeler/ifadeler  
        - 😠 → Küçümseme veya öfke içeren ifadeler  
        - 😐 → Duygu yüklü olmayan nötr içerik
        """)

# Yan panele eklemek için
with st.sidebar:
    show_help_section()
