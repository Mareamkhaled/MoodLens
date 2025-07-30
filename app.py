from flask import Flask, request, jsonify
from moodlens import analyze_mood  # your custom function

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the text input from Flutter
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Call your mood analysis function from moodlens.py
    mood, suggestions = analyze_mood(text)

    # Return the emotion and suggestions to the frontend
    return jsonify({
        'emotion': mood,
        'recommendations': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)