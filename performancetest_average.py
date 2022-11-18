"""import time
import json
import requests



def test_danish_with_lang_param():
    start = time.time()
    text = {
        "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
        "language": "da"
    }
    text_json = json.dumps(text)
    requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)

    return time.time()-start

def test_english_with_lang_param():
    start = time.time()
    text = {
        "string": "Hello, my name is Peter. I love cars and movies.",
        "language": "en"
    }
    text_json = json.dumps(text)
    requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)

    return time.time()-start

    start = time.time()
    text = {
def test_danish_no_lang_param():
        "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
    }
    text_json = json.dumps(text)
    requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)

    return time.time()-start

def test_english_no_lang_param():
    start = time.time()
    text = {
        "string": "Hello, my name is Peter. I love cars and movies."
    }
    text_json = json.dumps(text)
    requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)

    return time.time()-start

avg1,avg2,avg3,avg4 = 0,0,0,0
for i in range(100):
    avg1+=test_danish_with_lang_param()
avg1 = avg1/100

for i in range(100):
    avg2+=test_english_with_lang_param()
avg2 = avg2/100

for i in range(100):
    avg3+=test_danish_no_lang_param()
avg3 = avg3/100

for i in range(100):
    avg4+=test_english_no_lang_param()
avg4 = avg4/100

print("testDanishWithLangParam " + avg1)
print("testEnglishWithLangParam" + avg2)
print("testDanishNoLangParam" + avg3)
print("testEnglishNoLangParam" + avg4)
"""
