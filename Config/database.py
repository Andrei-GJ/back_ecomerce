from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from Models.base import Base

## Block for record (Models folder)
from Models.admin import Admin
from Models.category import Category
from Models.document_type import DocumentType
from Models.product import Product
from Models.users import User
from Models.provider import Provider
## Get environment variables
load_dotenv()
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

def inicializar_base_de_datos():
    print("Verificando y creando tablas en la base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("¡Tablas listas!")