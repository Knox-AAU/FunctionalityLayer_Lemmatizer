# Imported from spacy.io
import en_core_web_sm
import da_core_news_sm

def danishLemmatization(string):
    # Load the core module
    danLemma = da_core_news_sm.load()
    # Parse the string
    doc = danLemma(string)
    # Extract the lemma for each token and join the lemma with a space between every word. Then return it
    return " ".join([token.lemma_ for token in doc])

def englishLemmatization(string):
    # Same as in danishLemmatization()
    engLemma = en_core_web_sm.load()
    doc = engLemma(string)
    return " ".join([token.lemma_ for token in doc])

def Lemmatization(string, language):
    # Check which language to lemmatize and return the lemmatization
    if language == "da":return danishLemmatization(string)
    elif language == "en":return englishLemmatization(string)
    else: raise Exception("Language not implemented")