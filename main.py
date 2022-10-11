from fastapi import FastAPI
import uvicorn
import Lemmatization as lemma
from pydantic import BaseModel
from typing import Optional

# The parameter text that is going to be lemmatized is contained within a body

class Text(BaseModel):
    string: str
    language: Optional[str] = None

# Create an instance of FastAPI
app = FastAPI()

@app.post("/")
# Function that returns the lemmatized text
async def queryLemma(text: Text):
    return {"lemmatized_string": lemma.Lemmatization(text.string, text.language)}

@app.post("/GetLanguage")
async def getLanguage(text: Text):
    return {"lemmatized_language": lemma.get_language(text.string)}

# uvicorn controls which host and port the API is available at.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
