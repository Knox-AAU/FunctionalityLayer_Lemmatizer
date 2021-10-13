import requests
s = "[hej med dig & du er grim æ ø å]"
a = requests.get(f"http://130.225.57.27/lemmatizer/",params={"text":s})
print(a.content.decode())
