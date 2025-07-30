def analyze_mood(text):
    # Basic keyword-based mood detection
    mood = "happy" if "love" in text else "sad" if "tired" in text else "neutral"

    # Mock recommendations based on mood
    if mood == "happy":
        suggestions = ["Dance to music", "Call a friend", "Watch a comedy"]
    elif mood == "sad":
        suggestions = ["Take a walk", "Listen to soothing music", "Write in a journal"]
    else:
        suggestions = ["Explore something new", "Read a short article", "Stretch your legs"]

    return mood, suggestions