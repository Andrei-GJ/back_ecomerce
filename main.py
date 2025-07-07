from fastapi import FastAPI
from Config.database import Session, inicializar_base_de_datos
from Services.userServices import UserService
from Services.productServices import ProductService
import logging

app = FastAPI()

@app.get("/")
def root(): 
    return {"message": "Hello, World!"}

## Bloque de peticiones usuarios 
@app.get("/all_users")
def get_all_users():
    user_service = UserService(Session)
    try:
        users = user_service.get_all_users()
        return users
    except Exception as e:
        return {"error": str(e)}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user_service = UserService(Session)
    try:
        user = user_service.get_user_by_id(user_id)
        return user
    except Exception as e:
        return {"error": str(e)}

@app.post("/create_user")
def create_user(user_data: dict):
    user_service = UserService(Session)
    try:
        user = user_service.create_user(
            user_data["document_type_id"],
            user_data["document_number"],
            user_data["first_name"],
            user_data["surname"],
            user_data["email"]
        )
        return user
    except Exception as e:
        return {"error" : str(e)}

# ## Bloque de peticiones productos
@app.get("/all_products")
def get_all_products():
    product_service = ProductService(Session)
    try:
        products = product_service.get_all_products()
        return products
    except Exception as e:
        return {"error" : str(e)}

@app.get("/product/{product_id}")
def get_product_by_id(product_id : int):
    product_service = ProductService(Session)
    try:
        product = product_service.get_product_by_id(product_id)
        return product
    except Exception as e:
        return {"error" : str(e)}

@app.post("/create_product")
def create_product(product_data: dict):
    product_service = ProductService(Session)
    try:
        product = product_service.create_product(
            provider_id = ["provider_id"],
            category_id= ["category_id"],
            name_product= ["name_product"],
            quantity=["quantity"],
            isactive=["isactive"],
            price= ["price"],
            image= ["image"]
        )
        return product
    except Exception as e:
        return {"error" : str(e) }
    
# @app.get(off_product)
