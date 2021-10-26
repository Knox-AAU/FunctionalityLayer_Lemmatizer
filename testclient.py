import requests
import json


text = {
    "string": "Hej med dig",
}

textJson = json.dumps(text)
lemmatized_string = requests.post(
    f"http://knox-master01.srv.aau.dk/lemmatizer/", data=textJson)

print(lemmatized_string.content)
