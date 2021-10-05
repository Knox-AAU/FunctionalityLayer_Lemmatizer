import uvicorn
from fastapi import FastAPI
import Lemmatization as lemma

app = FastAPI()

@app.get("/lemma/{language}/{docs}")
async def queryLemma(docs:str,language:str):
    return {"docs": lemma.Lemmatization(docs,language)}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0", port=5000)