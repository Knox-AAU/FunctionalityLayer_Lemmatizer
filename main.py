from fastapi import FastAPI
import uvicorn
import Lemmatization as lemma
from pydantic import BaseModel

# The parameters needed is the language and text that is going to be lemmatized

class Text(BaseModel):
    string: str

# Create an instance of FastAPI
app = FastAPI()

@app.post("/")
# Function that returns the lemmatized text
async def queryLemma(text: Text):
    return {"lemmatized_string": lemma.Lemmatization(text.string)}

# uvicorn controls which host and port the API is available at.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
