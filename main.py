from fastapi import FastAPI
from Config.database import Session, inicializar_base_de_datos
from Services.userServices import UserService
import logging

app = FastAPI()

user_service = UserService(Session)

@app.get("/")
def root(): 
    return {"message": "Hello, World!"}

@app.get("/all_users")
def get_all_users():
    try:
        users = user_service.get_all_users()
        logging.info(f"Usuarios obtenidos: {users}")
        return users
    except Exception as e:
        logging.error(f"Error en /users: {e}")
        return {"error": e}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    try:
        users = user_service.get_user_by_id(user_id)
        logging.info(f"Usuarios obtenidos: {users}")
        return users
    except Exception as e:
        logging.error(f"Error en /users: {e}")
        return {"error": e}

@app.post("/create_user")
def create_user(user_data: dict):
    logging.info(user_data)
    logging.info(type(user_data))
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
        return {"error" : e}