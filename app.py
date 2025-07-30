from flask import Flask, request, jsonify
from moodlens import analyze_mood  # now powered by TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    mood, suggestions = analyze_mood(text)  # uses real sentiment scoring
    return jsonify({
        'emotion': mood,
        'recommendations': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)