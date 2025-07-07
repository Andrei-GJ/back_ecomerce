from fastapi import FastAPI
from Config.database import Session, inicializar_base_de_datos
from Services.userServices import UserService
from Services.productServices import ProductService
from Services.providerServices import ProviderService
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


# bloque de peticiones de proveedor
@app.get("/all_provider")
def all_provider():
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.get_all_providers()
        return provider
    except Exception as e:
        return {"error" : str(e)}

@app.get("/provider/{provider_id}")
def get_provider_by_id(provider_id):
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.get_provider_by_id(provider_id)
        return provider
    except Exception as e:
        return {"error" : str(e)}

@app.post("/create_provider")
def crete_provider(provider_data :dict):
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.create_provider(
            provider_data["name_provider"]
        )
        return provider
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
            product_data["provider_id"],
            product_data["category_id"],
            product_data["name_product"],
            product_data["quantity"],
            product_data["isactive"],
            product_data["price"],
            product_data["image"]
        )
        return product
    except Exception as e:
        return {"error" : str(e) }
    
# @app.get(off_product)
