import re
from spacy.language import Language
from spacy_language_detection import LanguageDetector
import da_core_news_sm
import en_core_web_sm

def lemmatization(string, language):
    if language == "da":
        nlp = da_core_news_sm.load()
        return get_trimmed_words(get_tokens(string), nlp)
    elif language == "en":
        nlp = en_core_web_sm.load()
        return get_trimmed_words(get_tokens(string), nlp)
    else:
        temp_language = da_core_news_sm.load()
        Language.factory("language_detector", func=get_lang_detector)
        temp_language.add_pipe("language_detector")
        doc = temp_language(string)
        input_language = doc._.language["language"]
        if input_language == 'da':
            nlp = da_core_news_sm.load()
            return get_trimmed_words(get_tokens(string), nlp)
        if input_language == 'en':
            nlp = en_core_web_sm.load()
            return get_trimmed_words(get_tokens(string), nlp)

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

def get_language(string):
    lemma = da_core_news_sm.load()
    dected_language = "da"
    Language.factory("language_detector", func=get_lang_detector)
    lemma.add_pipe("language_detector")
    doc = lemma(string.lower())
    if doc._.language["language"] == "en":
        lemma = en_core_web_sm.load()
        doc = lemma(string)
        dected_language = "en"
        return dected_language
    return "Language is not supported"

def get_lang_detector(nlp, name):
    return LanguageDetector()
