import unittest
import lemmatization as lemma


class wordcountTest(unittest.TestCase):

    def testDanishLemmatizatizer(self):
        f = open("testcases/testcase_da.txt", encoding='utf-8')
        string = f.read()
        f.close()
        answer = " ".join(word for word in string if word.isalnum())
        testcase = lemma.lemmatization(answer,"da")
        answer = answer.split(" ")
        testcase = testcase.split(" ")
        #print(len(testcase), len(answer))
        self.assertEqual(len(testcase), len(answer))

    def testEnglishLemmatizer(self):
        f = open("testcases/testcase_en.txt", encoding='utf-8')
        string = f.read()
        f.close()
        answer = " ".join(word for word in string if word.isalnum())
        testcase = lemma.lemmatization(answer,"en")
        answer = answer.split(" ")
        testcase = testcase.split(" ")
        # print(len(testcase),len(answer))
        self.assertEqual(len(testcase), len(answer))


if __name__ == '__main__':
    unittest.main()
