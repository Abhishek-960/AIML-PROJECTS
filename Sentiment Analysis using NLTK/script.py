import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# NLTK resources
nltk.download('vader_lexicon')

# 
mode = input(" Type '1' to enter your own text, or '2' for a sample: ")
if mode == '1':
    text = input("Enter your text: ")
else:
    text = "I am so happy today. The weather is beautiful and I feel amazing."

# Initialize sentiment analyzer
sid = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = sid.polarity_scores(text)
    compound = scores['compound']
    pos, neu, neg = scores['pos'], scores['neu'], scores['neg']
    lower_text = text.lower()

    # Strong Positive
    if compound >= 0.65:
        emotion = "joy 😊"

    # Strong Negative
    elif compound <= -0.65:
        if any(word in lower_text for word in ["hate", "rage", "beat", "angry"]):
            emotion = "anger 😠"
        elif any(word in lower_text for word in ["sad", "fail", "lonely", "bad"]):
            emotion = "sadness 😢"
        else:
            emotion = "negative sentiment 😞"

    # Hope and Motivation
    elif compound >= 0.4 and pos > 0.5:
        if any(word in lower_text for word in ["hope", "excited", "proud", "grateful", "overcome"]):
            emotion = "hopeful 🤞"
        else:
            emotion = "positive sentiment 🙂"

    # Neutral Zone
    elif -0.2 < compound < 0.2 and neu > 0.5:
        emotion = "neutral 😐"

    # Fear and Anxiety
    elif compound < -0.5 and any(word in lower_text for word in ["anxious", "scared", "nervous", "terrified"]):
        emotion = "fear 😨"

    # Disgust Detection
    elif "disgust" in lower_text or "gross" in lower_text or "nauseating" in lower_text:
        emotion = "disgust 🤢"

    else:
        emotion = "mixed emotion 🤔"
    
    return emotion

# Run detection
result = detect_emotion(text)
print(f"\n🔍 Detected Emotion: {result}")


