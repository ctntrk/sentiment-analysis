# 🎨 Dynamic Colorful Sentiment Analysis

This application uses **Streamlit** and the **Hugging Face Transformers** library to perform sentiment analysis on text input. The app analyzes the sentiment of the given text, displays the result, and dynamically changes the background color based on the sentiment detected.


## 🌐 Demo

You can try out the application and see it in action by visiting the link below:

[**Sentiment Analysis Demo**](https://dynamic-color-sentiment-analysis.streamlit.app)

---
## How It Works

## Streamlit Web Apps
![Alt text](https://github.com/ctntrk/sentiment-analysis/blob/main/recording-2025-03-20-13-53-13-0.jpg)

## Entering text with positive sentiment
![Alt text](https://github.com/ctntrk/sentiment-analysis/blob/main/recording-2025-03-20-13-53-13-1.jpg)
## Entering text with negative sentiment

![Alt text](https://github.com/ctntrk/sentiment-analysis/blob/main/recording-2025-03-20-13-53-13-2.jpg)

## Entering text with neutral sentiment
![Alt text](https://github.com/ctntrk/sentiment-analysis/blob/main/recording-2025-03-20-13-53-13-3.jpg)

---

## 📌 Project Overview

This project is a **web application** that allows users to input text and analyze its **sentiment**. The application displays the result with a corresponding **emoji**, **sentiment label** (Positive, Negative, Neutral), and a **confidence score**. Additionally, the background color changes dynamically based on the sentiment.

### Features:
- Real-time sentiment analysis
- Emotion-specific dynamic background color
- Display of sentiment label and confidence score
- Color transition animation

---

## 🔧 Technologies Used

- **Streamlit**: An open-source library for building interactive web applications with Python.
- **Transformers (Hugging Face)**: A library that provides pre-trained models for various NLP tasks, including sentiment analysis.
- **Python**: The primary programming language used in this project.
  
### Required Dependencies:
```bash
pip install streamlit==1.29.0
pip install transformers==4.49.0
pip install torch==2.6.0
```

---

## 🚀 Usage

1. To run the application, use the following command in the terminal:
   ```bash
   streamlit run app.py
   ```

2. **Enter text**: The user can input text into the input box to trigger the sentiment analysis.

3. **View results**: 
   - The app displays the sentiment analysis results, including an emoji and the sentiment label (e.g., Positive, Negative, Neutral).
   - The background color dynamically changes according to the sentiment.

---

## 🛠️ Technical Details

### Model
The application uses the **cardiffnlp/twitter-roberta-base-sentiment** model, a pre-trained model for Twitter sentiment analysis that classifies text into three sentiment categories:
- **Positive**
- **Negative**
- **Neutral**

### Color and Emoji Codes

- **Positive Sentiment**:  
  - Color: `#90EE90` (Light Green)  
  - Emoji: `😊`
  
- **Negative Sentiment**:  
  - Color: `#FF6B6B` (Light Red)  
  - Emoji: `😠`
  
- **Neutral Sentiment**:  
  - Color: `#FFD93D` (Light Yellow)  
  - Emoji: `😐`

### Confidence Score
For each sentiment prediction, the model provides a **confidence score**, which indicates the model’s certainty about its prediction. This score ranges from 0 to 1, with higher values indicating greater confidence.

---

## 📖 Help and Information

### Help Section
The app features a **Help** section in the sidebar that explains:
- **Confidence Score**: The model's confidence in the prediction (range 0-1).
- **Quick Guide**: A simple guide to understanding the sentiment labels and their corresponding emojis and colors.
- **Detailed Technical Information**: An explanation of how the model works, color codes, and emoji symbolism.

### Detailed Technical Information
- **Confidence Score**:
  - Calculation Method: Directly taken from the model’s output (`result['score']`).
  - Interpretation: 0.0-0.4 → Low confidence, 0.4-0.6 → Medium confidence, 0.6-1.0 → High confidence.
- **Color Codes**:
  - Positive: `#90EE90` (Light Green)
  - Negative: `#FF6B6B` (Light Red)
  - Neutral: `#FFD93D` (Light Yellow)
- **Emoji Symbolism**:
  - 😊 → Positive expressions
  - 😠 → Negative or angry expressions
  - 😐 → Emotionally neutral content

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
