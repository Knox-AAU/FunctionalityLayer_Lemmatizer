# Imported from spacy.io
import da_core_news_sm
import en_core_web_sm
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


def Lemmatization(string, language):
        if language == "da":
            Lemma = da_core_news_sm.load()
            doc = Lemma(string.lower())
            return " ".join([token.lemma_ for token in doc])

        elif language == "en":
            Lemma = en_core_web_sm.load()
            doc = Lemma(string)
            return " ".join([token.lemma_ for token in doc])

        else:
            
            try:
                Lemma = da_core_news_sm.load()
                Language.factory("language_detector", func=get_lang_detector)
                Lemma.add_pipe("language_detector")
                dected_language = "da"
                try:
                    doc = Lemma(string.lower())
                    if doc._.language["language"] == "en":
                        Lemma = en_core_web_sm.load()
                        doc = Lemma(string)
                        dected_language = "en"

                    return " ".join([token.lemma_ for token in doc])

                except Exception as e:
                    return str(e)

            except Exception as e:
                return str(e)

def get_lang_detector(nlp, name):
    return LanguageDetector()
