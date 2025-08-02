def get_activity_suggestion(emotion, entities):
    suggestions = {
        "joyful": "Celebrate with something fun like dancing or journaling your joy!",
        "upset": "Try a calming activity like deep breathing or listening to soft music.",
        "angry": "Consider a physical outlet like a walk or expressive drawing.",
        "concerned": "Ground yourself with mindfulness or talk to someone you trust.",
        "neutral": "Explore something new or reflect quietly.",
        "frustrated": "Take a break, stretch, or write down what’s bothering you."
    }

    return suggestions.get(emotion, "Take a moment to pause and reflect.")