# Imported from spacy.io
import da_core_news_sm
import en_core_web_sm
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


def Lemmatization(string):
    # Same as in danishLemmatization()
    try:
        Lemma = en_core_web_sm.load()
        Language.factory("language_detector", func=get_lang_detector)
        Lemma.add_pipe("language_detector")

        try:
            doc = Lemma(string)
            if doc._.language["language"] == "da":
                Lemma = da_core_news_sm.load()
                doc = Lemma(string)

            return " ".join([token.lemma_ for token in doc])
        except Exception as e:
            return str(e)
    except Exception as e:
        return str(e)


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42
