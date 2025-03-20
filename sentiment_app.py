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

st.set_page_config(page_title="Sentiment Analysis", layout="wide")
st.title("🎨 Dynamic Colorful Sentiment Analysis")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("""
    **Used Model:**  
    `cardiffnlp/twitter-roberta-base-sentiment`  
    (3-class Twitter sentiment analysis model)
    
    **Color Coding:**
    - 🟢 Positive: #90EE90 (Light Green)
    - 🔴 Negative: #FF6B6B (Light Red)
    - 🟡 Neutral: #FFD93D (Light Yellow)
    """)
    
    st.header("ℹ️ Information Panel")
    st.markdown("""
    **Application Features:**
    - Real-time sentiment analysis based on text input
    - Emotion-specific dynamic background color
    - Sentiment label and confidence score display
    - Color transition animation
    """)

user_input = st.text_input("Enter text:", "")

if user_input:
    classifier = load_model()
    result = classifier(user_input)[0]
    
    # Label conversion
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
        st.subheader(f"{EMOJI_MAP[label]} Result: {label}")
    with col2:
        st.metric("Confidence Score", f"{result['score']:.2%}")

else:
    st.info("Please enter some text")

def show_help_section():
    st.sidebar.subheader("📖 Help & Information")
    
    # Basic help information
    st.sidebar.markdown("""
    **Confidence Score:**  
    Model's confidence in prediction (0-1 range, higher = more confident)
    
    **Quick Guide:**  
    - 😊 Positive Sentiment  
    - 😠 Negative Sentiment  
    - 😐 Neutral Sentiment  
    - Colors change automatically based on sentiment
    """)
    
    # Detailed information expander
    with st.sidebar.expander("📊 Detailed Technical Information"):
        st.markdown("""
        **Confidence Score**
        - **Calculation Method:** Directly taken from model outputs (`result['score']`)
        - **Interpretation:**  
          0.0-0.4 → Low confidence  
          0.4-0.6 → Medium confidence  
          0.6-1.0 → High confidence

        **Color Codes**  
        | Sentiment | HEX Code    | Example     |
        |-----------|-------------|-------------|
        | Positive  | `#90EE90`   | 🟩 Light Green |
        | Negative  | `#FF6B6B`   | 🟥 Light Red |
        | Neutral   | `#FFD93D`   | 🟨 Light Yellow |

        **Emoji Symbolism**  
        - 😊 → Positive words/expressions  
        - 😠 → Derogatory or angry expressions  
        - 😐 → Emotionally neutral content
        """)

# Add to sidebar
with st.sidebar:
    show_help_section()
