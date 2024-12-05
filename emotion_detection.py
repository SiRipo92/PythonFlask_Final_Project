import requests
import json

def emotion_detector(text_to_analyse):
    """Function to analyze emotion from text using the Watson NLP library.

    Args:
        text_to_analyse (str): The text to be analyzed for emotions.

    Returns:
        str: The text attribute of the response object from the Emotion Detection function.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } } # Create dictionary w/ text to be analyzed
    
    # Send POST request to the API with text
    response = requests.post(url, json = myobj, headers=headers ) # Send POST request to the API w/ text

    # Parse response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    # ["emotionPredictions"] accesses the top-level key in the dict containing the list of predictions
    # [0] selects the 1st element of the list, being emotions, which is a dictionary of emotions
    # ["emotions"] accesses the emotion dict inside the 1st prediction where indv. emotion scores are stored
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the emotions as a dictionary with their corresponding scores and dominant emotion
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }