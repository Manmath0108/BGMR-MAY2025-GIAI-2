import json

from fastapi import FastAPI, HTTPException
from starlette.responses import Response
import uvicorn

from app.api.api import read_user, read_questions
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fast API in python"}

BASE_DIR = "/home/manmath/PycharmProjects/BGMR-MAY2025-GIAI-2/"

@app.post("/alternatives")
def read_alternatives(id: int):
    with open(f"{BASE_DIR}data/alternatives.json") as stream:
        alternatives = json.load(stream)
    for questions in alternatives:
        if questions['question_id'] == id:
            result = questions.get('alternative')
            print(result)
            return result
if __name__ == "__main__":
    read_alternatives(3)
    uvicorn.run(app,port=5002)



