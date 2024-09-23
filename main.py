import fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello_bravo():
    return {"msg": "Hello BravoShop"}
