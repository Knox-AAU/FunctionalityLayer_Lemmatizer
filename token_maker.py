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

def get_trimmed_words(tokens, nlp):
    tokens_str = ' '.join(tokens)
    doc = nlp(tokens_str)
    tokens_lemmas = []
    for token in doc:
        if not token.is_stop:
            tokens_lemmas.append(token.lemma_)
    return tokens_lemmas

def get_tokens(text):
    text = text.lower()
    accepted_tokens_pattern = get_token_re_pattern()
    tokens = []
    for match in accepted_tokens_pattern.finditer(text):
        tokens.append(match.group())
    return tokens

def get_token_re_pattern():
    return re.compile(r'[0-9]+,[0-9]+|[a-z0-9æøå]{2,}|[0-9]+')

def get_language(input_str):
    lemma = da_core_news_sm.load()
    Language.factory("language_detector", func=get_lang_detector)
    lemma.add_pipe("language_detector")
    doc = lemma(input_str.lower())
    if doc._.language["language"] is not None:
        return doc._.language["language"]
    else:
        return "Can not recognise language "

def get_lang_detector(nlp, name):
    return LanguageDetector()
