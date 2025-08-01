from textblob import TextBlob
from langdetect import detect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline
import nltk

# Download VADER lexicon if not already present
nltk.download('vader_lexicon')

# Initialize sentiment models
vader = SentimentIntensityAnalyzer()
transformer_sentiment = pipeline("sentiment-analysis")

def analyze_mood(text):
    emotion = classify_emotion(text)
    recommendations = get_recommendations(emotion)
    color = get_mood_color(emotion)
    return emotion, recommendations["suggestions"], recommendations["activity"], color

def classify_emotion(text):
    lower_text = text.lower()
    lang = detect(text)

    # Keyword-based cues
    keywords = {
        "frustrated": ["tried fixing", "still won’t work", "what’s even the point", "ugh", "fed up", "give up", "overwhelmed", "burned out"],
        "angry": ["ridiculous", "i’m done", "can’t stand", "infuriating", "rage", "furious", "hate", "so mad"],
        "joyful": ["excited", "overjoyed", "ecstatic", "thrilled", "so happy", "elated", "grinning"],
        "calm": ["peaceful", "relaxed", "serene", "quiet", "restful", "chill"],
        "content": ["satisfied", "grateful", "comfortable", "pleased", "fine", "okay", "alright"],
        "upset": ["sad", "hurt", "disappointed", "زعلان", "تعبان", "tired", "heartbroken", "exhausted", "drained", "lonely", "down"]
    }

    for emotion, cues in keywords.items():
        if any(phrase in lower_text for phrase in cues):
            return emotion

    # Arabic fallback
    if lang == "ar":
        if "زعلان" in lower_text or "تعبان" in lower_text:
            return "upset"
        elif "فرحان" in lower_text or "مبسوط" in lower_text:
            return "joyful"
        else:
            return "neutral"

    # English fallback: VADER + Transformer
    vader_score = vader.polarity_scores(text)
    compound = vader_score['compound']

    transformer_result = transformer_sentiment(text)[0]
    label = transformer_result['label']
    confidence = transformer_result['score']

    # Intensity scoring
    if label == "POSITIVE":
        if compound > 0.7 and confidence > 0.9:
            return "joyful"
        elif compound > 0.4:
            return "content"
        else:
            return "calm"
    elif label == "NEGATIVE":
        if compound < -0.7 and confidence > 0.9:
            return "angry"
        elif compound < -0.4:
            return "frustrated"
        else:
            return "upset"
    else:
        return "neutral"

def get_mood_color(emotion):
    colors = {
        "joyful": "#FFD700",       # gold
        "content": "#FFB6C1",      # light pink
        "calm": "#ADD8E6",         # light blue
        "angry": "#DC143C",        # crimson
        "frustrated": "#FF6347",   # tomato
        "upset": "#800080",        # purple
        "neutral": "#D3D3D3"       # light gray
    }
    return colors.get(emotion, "#FFFFFF")  # default white

def get_recommendations(emotion):
    suggestions = {
        "joyful": [
            "Celebrate a small win",
            "Share your happiness with someone",
            "Take a moment to savor it"
        ],
        "content": [
            "Maintain your positive momentum",
            "Reflect on what’s working well",
            "Reward yourself with rest"
        ],
        "calm": [
            "Enjoy the peaceful vibe",
            "Try meditative breathing",
            "Spend time in nature"
        ],
        "angry": [
            "Take a break from the trigger",
            "Channel the energy into action",
            "Try writing out your thoughts"
        ],
        "frustrated": [
            "Pause and regroup",
            "Break tasks into smaller steps",
            "Seek input or a second opinion"
        ],
        "upset": [
            "Talk to someone you trust",
            "Do something comforting",
            "Give yourself permission to feel"
        ],
        "neutral": [
            "Reflect or journal if you'd like",
            "Explore something new",
            "Do a self-check-in"
        ]
    }

    activity = {
        "joyful": "Go for a walk with music or dance around your room 🎶",
        "content": "Make a gratitude list or enjoy a cozy drink ☕",
        "calm": "Try a 5-minute meditation or light stretching 🧘",
        "angry": "Do a quick workout or write in a journal 🏋️",
        "frustrated": "Sketch something random or organize your space ✏️",
        "upset": "Watch a comfort movie or call a friend 📞",
        "neutral": "Try something new like a podcast or a short walk 🚶"
    }

    return {
        "suggestions": suggestions.get(emotion, ["Take a moment to reflect."]),
        "activity": activity.get(emotion, "Do something that feels right for you.")
    }