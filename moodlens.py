from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Range: -1.0 (negative) to 1.0 (positive)

    # Classify mood based on polarity
    if polarity > 0.3:
        mood = "happy"
        suggestions = ["Celebrate a small win", "Dance to music", "Plan something fun"]
    elif polarity < -0.3:
        mood = "sad"
        suggestions = ["Journal your thoughts", "Listen to calming music", "Try guided breathing"]
    else:
        mood = "neutral"
        suggestions = ["Explore something new", "Read a short article", "Stretch your legs"]

    return mood, suggestions