import requests
import threading
import time
import json



def testDanishWithLangParam(self):
    start = time.time()
    text = {
        "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
        "language": "da"
    }
    textJson = json.dumps(text)
    lemmatized_string = requests.post(
        f"http://127.0.0.1:5000/", data=textJson)

    return time.time()-start

def testEnglishWithLangParam(self):
    start = time.time()
    text = {
        "string": "Hello, my name is Peter. I love cars and movies.",
        "language": "en"
    }
    textJson = json.dumps(text)
    lemmatized_string = requests.post(
        f"http://127.0.0.1:5000/", data=textJson)

    return time.time()-start

def testDanishNoLangParam(self):
    start = time.time()
    text = {
        "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
    }
    textJson = json.dumps(text)
    lemmatized_string = requests.post(
        f"http://127.0.0.1:5000/", data=textJson)

    return time.time()-start

def testEnglishNoLangParam(self):
    start = time.time()
    text = {
        "string": "Hello, my name is Peter. I love cars and movies."
    }
    textJson = json.dumps(text)
    lemmatized_string = requests.post(
        f"http://127.0.0.1:5000/", data=textJson)

    return time.time()-start

avg1,avg2,avg3,avg4 = 0,0,0,0
for i in range(100):
    avg1+=testDanishWithLangParam()
avg1 = avg1/100;

for i in range(100):
    avg2+=testEnglishWithLangParam()
avg2 = avg2/100;

for i in range(100):
    avg3+=testDanishNoLangParam()
avg3 = avg3/100;

for i in range(100):
    avg4+=testEnglishNoLangParam()
avg4 = avg4/100;

print("testDanishWithLangParam " + avg1)
print("testEnglishWithLangParam" + avg2)
print("testDanishNoLangParam" + avg3)
print("testEnglishNoLangParam" + avg4)
