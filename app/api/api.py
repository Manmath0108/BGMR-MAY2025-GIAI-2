import json
from fastapi import FastAPI, HTTPException
from starlette.responses import Response
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fast API in python"}

BASE_DIR = "/home/manmath/PycharmProjects/BGMR-MAY2025-GIAI-2/"

@app.post("/read_user")
def read_user():
    with open(f"{BASE_DIR}data/users.json") as stream:
        users = json.load(stream)
        return users

@app.post("/read_question")
def read_questions(position: int):
    with open(f"{BASE_DIR}data/questions.json") as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            res = question.get('question')
            print(res)
            return res

if __name__ == "__main__":
    print(read_user())
    read_questions(2)
    uvicorn.run(app, port=5003)


