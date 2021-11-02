import Lemmatization as lemma
import unittest
import requests
import json
import threading
import time
class testClient(unittest.TestCase):

    def testRespons(self):
        start = time.time()
        text = {
            "string": "Hej med dig",
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)
        print(lemmatized_string.status_code)
        print("Test with no language in body and written in Danish:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)
        
    def testLenght(self):
        text = {
            "string": "Hej med dig",
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)
        print(lemmatized_string.content)
        self.assertEqual(len(str(lemmatized_string.content).split(" ")), len(text["string"].split(" ")))    

    def testDa(self):
        start = time.time()
        text = {
            "string": "Hej med dig",
            "language": "da"
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)
        print(lemmatized_string.status_code)
        print("Test with language in body:", time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def testEn(self):
        start = time.time()
        text = {
            "string": "This is better from this side",
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)
        print(lemmatized_string.status_code)
        print("Test with no language in body and written in English:", time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)


if __name__ == '__main__':
    unittest.main()


