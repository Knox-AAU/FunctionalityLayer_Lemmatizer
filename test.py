import unittest
import Lemmatization as lemma


class wordcountTest(unittest.TestCase):

    def testDanishLemmatizatizer(self):
        string = "hahahahahahahahha jeg er så sjov :D"
        answer = " ".join(word for word in string if word.isalnum())
        testcase = lemma.Lemmatization(answer,"da")
        answer = answer.split(" ")
        testcase = testcase.split(" ")
        #print(len(testcase), len(answer))
        self.assertEqual(len(testcase), len(answer))

    def testEnglishLemmatizer(self):
        string = "hahahahhahahahah im so funny :D"
        answer = " ".join(word for word in string if word.isalnum())
        testcase = lemma.Lemmatization(answer,"en")
        answer = answer.split(" ")
        testcase = testcase.split(" ")
        # print(len(testcase),len(answer))
        self.assertEqual(len(testcase), len(answer))


if __name__ == '__main__':
    unittest.main()
