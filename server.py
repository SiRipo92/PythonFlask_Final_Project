# Import necessary packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route('/')
def index():
    # Serve the main page (index.html)
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotion of the given statement and return the formatted response."""
    # Retrieve the text to analyze from the form
    statement = request.args.get('textToAnalyze')

    # Check if the statement is empty or None
    if not statement or statement.strip() == "":
        return "Invalid text! Please try again.", 400
       
    # Call the emotion_detector function with the text
    result = emotion_detector(statement)

    # If all emotions are None (meaning invalid input detected by the model), return an error
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400

    # Format the response string as required
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
   
    # Return the formatted response as plain text
    return formatted_response

if __name__ == '__main__':
    app.run(debug=True)
