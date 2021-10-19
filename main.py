from fastapi import FastAPI
import uvicorn
import Lemmatization as lemma

# Create an instance of FastAPI
app = FastAPI()

# Handles the path and the GET request 
# The parameters needed is the language and text that is going to be lemmatized
@app.get("/")
# Function that returns the lemmatized text
async def queryLemma(text:str="",language:str="da"):
    try:return {"lemmatized_text": lemma.Lemmatization(text,language)}
    except:return Exception.message

# uvicorn controls which host and port the API is available at.
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0", port=5000)