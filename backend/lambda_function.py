import json
import requests

def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])
        text = body.get("text", "")
        target_lang = body.get("target_language", "en")

        url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
        response = requests.get(url).json()
        translated_text = response["responseData"]["translatedText"]

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({
                "original_text": text,
                "translated_text": translated_text,
                "target_language": target_lang
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
