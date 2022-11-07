"""import unittest
import requests
import threading
import time
import json


class testPerformance(unittest.TestCase):

    def testDanishWithLangParam(self):
        start = time.time()
        text = {
            "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
            "language": "da"
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)

        print("Language given, danish text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def testEnglishWithLangParam(self):
        start = time.time()
        text = {
            "string": "Hello, my name is Peter. I love cars and movies.",
            "language": "en"
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)

        print("Language given, english text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def testDanishNoLangParam(self):
        start = time.time()
        text = {
            "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)

        print("Language not given, danish text:",
                time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def testEnglishNoLangParam(self):
        start = time.time()
        text = {
            "string": "Hello, my name is Peter. I love cars and movies."
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)

        print("Language not given, english text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)


if __name__ == '__main__':
    unittest.main()
"""
