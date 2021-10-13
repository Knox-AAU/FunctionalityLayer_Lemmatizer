import requests
string = "The lemmatization of this string is very good! Should we make it available for everyone? Yes we should."
lemmatized_string = requests.get(f"http://130.225.57.27/lemmatizer/", params={"text": string, "language": "en"})
print(lemmatized_string.content.decode())