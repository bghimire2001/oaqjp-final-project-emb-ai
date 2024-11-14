from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Return a formatted string with the sentiment label and score
    d1 = dict(list(response.items())[5:])
    d2 = dict(list(response.items())[:5]).__str__()[1:-1]
    if d1['dominant_emotion'] != 'None':
        return "For the given statement, the system response is {} . The dominant emotion is {}.".format(d2, d1['dominant_emotion'])

    else:
        return "Invalid Text! Please try again"


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)