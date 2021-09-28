import en_core_web_sm
import da_core_news_sm
import json

#jsonTest= {"Title:":"Lol","Year":"2013","Text":"This is a test for the lemmatizer"}

def danishLemmatization(string):
    danLemma = da_core_news_sm.load()
    doc = danLemma(string)

    return " ".join([token.lemma_ for token in doc])

def englishLemmatization(string):
    engLemma = en_core_web_sm.load()
    doc = engLemma(string)

    return " ".join([token.lemma_ for token in doc])
