import en_core_web_sm
import da_core_news_sm

def danishLemmatization(string):

    danLemma = da_core_news_sm.load()
    doc = danLemma(string)

    return " ".join([token.lemma_ for token in doc])

def englishLemmatization(string):

    engLemma = en_core_web_sm.load()
    doc = engLemma(string)

    return " ".join([token.lemma_ for token in doc])

def Lemmatization(string, language):
    
    if language == "da":return danishLemmatization(string)
    elif language == "en":return englishLemmatization(string)