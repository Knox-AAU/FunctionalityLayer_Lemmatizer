import uvicorn
from fastapi import FastAPI
import Lemmatization as lemma
import json

app = FastAPI()

@app.get("/lemma/{docs}")
async def queryLemma(docs:str):
    return {"docs": lemma.danishLemmatization(docs)}

async def jsonLemma(docs:json):
    return {"docs": docs}
if __name__=="__main__":
    print("hej")
    uvicorn.run(app,host="0.0.0.0", port=5000)

