from flask import Flask, request, jsonify
from moodlens import analyze_mood  # Imports your upgraded logic

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    mood, suggestions,activity ,color = analyze_mood(text)
    return jsonify({
        'emotion': mood,
        'recommendations': suggestions,
        'color': color,
        'activity': activity
    })

if __name__ == '__main__':
    app.run(debug=True)