from fastapi import FastAPI
from starlette.responses import Response
import uvicorn

app = FastAPI()
@app.get("/")
def root():
    return  {"message": "FastAPI in python"}
@app.post("/add")
def add(a, b):
    a = float(a)
    b = float(b)
    return a+b
@app.post("/sub")
def sub(a, b):
    a = float(a)
    b = float(b)
    return a-b

if __name__ == "__main__":
    print(add(1,2))
    print(sub(4, 5))
uvicorn.run(app, port=5001)