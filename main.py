from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
import token_maker


# The parameter text that is going to be lemmatized is contained within a body

class Text(BaseModel):
    string: str
    language: Optional[str] = None
# Create an instance of FastAPI
app = FastAPI()

# Function that returns the lemmatized text
@app.post("/")
async def query_lemma(text: Text):
    return token_maker.lemmatization(text.string, text.language)

# Function that returns the language of the text
@app.post("/GetLanguage")
async def get_language(text: Text):
    return {"lemmatized_language": token_maker.get_language(text.string)}

# uvicorn controls which host and port the API is available at.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
