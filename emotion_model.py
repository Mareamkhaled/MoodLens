from transformers import pipeline

# Load the emotion classification model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    # return_all_scores=False
)

def detect_model_emotion(text):
    result = emotion_classifier(text)
    label = result[0]['label'].lower()  # e.g. "sadness", "joy", "anger"
    
    # Map model labels to your app's emotion categories
    label_map = {
        "joy": "joyful",
        "sadness": "upset",
        "anger": "angry",
        "fear": "concerned",
        "surprise": "neutral",
        "disgust": "frustrated"
    }

    return label_map.get(label, "neutral")