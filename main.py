from fastapi import FastAPI
from Config.database import Session, inicializar_base_de_datos

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/products")
def get_products():
    return {"products": []}
