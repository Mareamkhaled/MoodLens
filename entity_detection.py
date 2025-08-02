def extract_entities(text):
    entities = []
    keywords = ["exam", "mother", "father", "friend", "deadline", "project", "school", "work", "grandma"]
    for word in keywords:
        if word in text.lower():
            entities.append(word)
    return entities