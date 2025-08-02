def get_empathetic_message(emotion):
    messages = {
        "joyful": "That’s wonderful to hear! Let’s hold onto that feeling.",
        "upset": "I’m really sorry you’re feeling this way. You’re not alone.",
        "angry": "It’s okay to feel angry. Let’s find a way to release it safely.",
        "concerned": "It sounds like something’s weighing on you. I’m here for you.",
        "neutral": "Thanks for sharing. Let’s explore what might help you feel more centered.",
        "frustrated": "That sounds tough. Let’s take a breath and reset together."
    }

    return messages.get(emotion, "I’m here to support you.")


def get_follow_up_question(emotion):
    questions = {
        "joyful": "What’s bringing you joy today?",
        "upset": "Would you like to talk more about what’s troubling you?",
        "angry": "What triggered this feeling for you?",
        "concerned": "Is there something specific that’s causing worry?",
        "neutral": "Would you like to explore how you’re feeling more deeply?",
        "frustrated": "What’s been making things feel difficult lately?"
    }

    return questions.get(emotion, "Want to share more about what’s on your mind?")