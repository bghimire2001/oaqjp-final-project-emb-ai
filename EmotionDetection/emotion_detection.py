import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = inputs, headers = headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        result = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(result, key=result.get)
        result['dominant_emotion'] = dominant_emotion

    elif response.status_code == 400: 
        result = { "anger": 'None', "disgust": 'None', "fear": 'None', 
        "joy": 'None',"sadness": 'None', "dominant_emotion":'None'}
    return result