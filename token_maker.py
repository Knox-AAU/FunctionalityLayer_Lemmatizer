import re
from spacy.language import Language
from spacy_language_detection import LanguageDetector
import da_core_news_sm
import en_core_web_sm

def lemmatization(input_str, language):
    if language is None:
        language = get_language(input_str)
    if language == "da":
        nlp = da_core_news_sm.load()
        return get_trimmed_words(get_tokens(input_str), nlp)
    elif language == "en":
        nlp = en_core_web_sm.load()
        return get_trimmed_words(get_tokens(input_str), nlp)
    else:
        return "Text is not of a supported language"

def get_trimmed_words(words, nlp):
    words_str = ' '.join(words)
    doc = nlp(words_str)
    word_lemmas = []
    for token in doc:
        if not token.is_stop:
            word_lemmas.append(token.lemma_)
    return word_lemmas

def get_tokens(text):
    text = text.lower()
    accepted_tokens_pattern = get_token_re_pattern()
    words = []
    for match in accepted_tokens_pattern.finditer(text):
        words.append(match.group())
    return words

def get_token_re_pattern():
    return re.compile(r'[0-9]+,[0-9]+|[a-z0-9æøå]{2,}|[0-9]+')

def get_language(input_str):
    lemma = da_core_news_sm.load()
    dected_language = "da"
    Language.factory("language_detector", func=get_lang_detector)
    lemma.add_pipe("language_detector")
    doc = lemma(input_str.lower())
    if doc._.language["language"] == "en":
        lemma = en_core_web_sm.load()
        doc = lemma(input_str)
        dected_language = "en"
        return dected_language
    else:
        return "Language is not supported"

def get_lang_detector(nlp, name):
    return LanguageDetector()
