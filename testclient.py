import Lemmatization as lemma
import unittest
import requests
import json

class testClient(unittest.TestCase):

    def testRespons(self):
        text = {
            "string": "Hej med dig",
        }
        textJson = json.dumps(text)
        lemmatized_string = requests.post(
            f"http://127.0.0.1:5000/", data=textJson)
        print(lemmatized_string.status_code)
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


if __name__ == '__main__':
    unittest.main()


