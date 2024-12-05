import requests

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

    # Return the text attribute of the response object
    return response.text