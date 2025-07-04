## 🧠 Emotion Detection in Text — VADER-Powered Sentiment Analyzer

This Python project leverages NLTK’s VADER Sentiment Analyzer to classify emotional tone from natural language input. Users can enter their own text or let the system generate a sample, and the model returns an emotion label such as joy, sadness, anger, hopeful, and more.

## 🎯 Key Features
📝 Interactive user input or auto-generated statements
🔍 Emotion classification using VADER compound and polarity scores
🎭 Advanced detection for joy, sadness, anger, hopeful, love, fear, disgust, and neutral
🧠 Context-aware keyword mapping for richer emotional nuance
📊 Sentiment breakdown printed for every prediction

## 🧪 How It Works
NLTK’s VADER lexicon assigns sentiment scores to the text.
Scores include:
pos: proportion of positive sentiment
neg: proportion of negative sentiment
neu: proportion of neutral sentiment
compound: overall sentiment from –1 (most negative) to +1 (most positive)

## Results
![abhi 5](https://github.com/user-attachments/assets/a898b752-425f-48b4-a07c-5d3f81d0e5ab)


## 📦 Installation Instructions
bash
pip install nltk
Then download the required sentiment resources once inside Python:
python
import nltk
nltk.download('vader_lexicon')

## ▶️ How to Use
bash : python script.py
Choose:

1 to enter your own sentence
2 to test using built-in sample statement

Get output:
📊 Sentiment breakdown with polarity scores
🔍 Final emotion label (with emoji)
