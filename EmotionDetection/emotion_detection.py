import requests
import json

def emotion_detector(text_to_analyse):
    """Function to analyze emotion from text using the Watson NLP library.

    Args:
        text_to_analyse (str): The text to be analyzed for emotions.

    Returns:
        str: The text attribute of the response object from the Emotion Detection function.
    """
    # Check if the text is empty or None before making the request
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    
    # Send POST request to the API with text
    response = requests.post(url, json = myobj, headers=headers )

   # If status code is 200, extract emotion data
    if response.status_code == 200:
        # Parse the response text into a dictionary
        formatted_response = json.loads(response.text)
        
        # Extract emotion scores from the response
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Find the dominant emotion (the one with the highest score)
        dominant_emotion = max(emotions, key=emotions.get, default=None)

        return {
            "anger": emotions.get("anger"),
            "disgust": emotions.get("disgust"),
            "fear": emotions.get("fear"),
            "joy": emotions.get("joy"),
            "sadness": emotions.get("sadness"),
            "dominant_emotion": dominant_emotion
        }
    
    # If the response status code is 500 or any other error
    elif response.status_code == 500:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    # For other response codes, return None values as fallback
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }