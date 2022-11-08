"""import unittest
import json
import time
import requests


class TestPerformance(unittest.TestCase):

    def test_danish_with_lang_param(self):
        start = time.time()
        text = {
            "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
            "language": "da"
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post(
            "http://127.0.0.1:5000/", data=text_json, timeout=10)

        print("Language given, danish text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def test_english_with_lang_param(self):
        start = time.time()
        text = {
            "string": "Hello, my name is Peter. I love cars and movies.",
            "language": "en"
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post(
            "http://127.0.0.1:5000/", data=text_json, timeout=10)

        print("Language given, english text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def test_danish_no_lang_param(self):
        start = time.time()
        text = {
            "string": "Hej, mit navn er Peter. Jeg elsker biler og film.",
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post(
            "http://127.0.0.1:5000/", data=text_json, timeout=10)

        print("Language not given, danish text:",
                time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)

    def test_english_no_lang_param(self):
        start = time.time()
        text = {
            "string": "Hello, my name is Peter. I love cars and movies."
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post(
            "http://127.0.0.1:5000/", data=text_json, timeout=10)

        print("Language not given, english text:",
              time.time()-start)
        self.assertEqual(lemmatized_string.status_code, 200)


if __name__ == '__main__':
    unittest.main()
"""
