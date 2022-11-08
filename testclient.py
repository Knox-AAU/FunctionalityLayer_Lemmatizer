"""import unittest
import json
import requests

class TestClient(unittest.TestCase):

    def test_respons(self):
        text = {
            "string": "Hej med dig",
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)
        print(lemmatized_string.status_code)
        self.assertEqual(lemmatized_string.status_code, 200)

    def test_lenght(self):
        text = {
            "string": "Hej med dig",
        }
        text_json = json.dumps(text)
        lemmatized_string = requests.post("http://127.0.0.1:5000/", data=text_json, timeout=10)
        print(lemmatized_string.content)
        self.assertEqual(len(str(lemmatized_string.content).split(" ")), len(text["string"].split(" ")))


if __name__ == '__main__':
    unittest.main()
"""
