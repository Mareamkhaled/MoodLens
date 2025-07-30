from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    emotion = classify_emotion(polarity)
    recommendations = get_recommendations(emotion)
    color = get_mood_color(emotion)

    return emotion, recommendations, color

def classify_emotion(polarity):
    if polarity > 0.6:
        return "joyful"
    elif polarity > 0.3:
        return "content"
    elif polarity > 0.1:
        return "calm"
    elif polarity < -0.6:
        return "angry"
    elif polarity < -0.3:
        return "frustrated"
    elif polarity < -0.1:
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
    return suggestions.get(emotion, ["Take a moment to reflect."])