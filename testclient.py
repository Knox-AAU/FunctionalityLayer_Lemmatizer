import requests
import json
text = {
    "string": "Hej med dig",
    "language": "da"
}

textJson = json.dumps(text)
lemmatized_string = requests.post(
    f"http://130.225.57.27/lemmatizer/", Text=textJson)
print(lemmatized_string.content.decode())
