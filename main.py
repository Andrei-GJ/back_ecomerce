from operator import truediv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Config.database import Session, inicializar_base_de_datos
from Services.userServices import UserService
from Services.productServices import ProductService
from Services.providerServices import ProviderService
from Services.categoryServices import CategoryService
import logging

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Inicializar la base de datos al arrancar la aplicación
try:
    inicializar_base_de_datos()
    print("Base de datos inicializada correctamente")
except Exception as e:
    print(f"Error al inicializar la base de datos: {e}")
    logging.error(f"Database initialization error: {e}")

@app.get("/")
def root(): 
    return {"message": "Hello, World!"}


# =====================
# Bloque de peticiones usuarios
# =====================
@app.get("/all_users")
def get_all_users():
    """Lista todos los usuarios del sistema"""
    user_service = UserService(Session)
    try:
        users = user_service.get_all_users()
        return users
    except Exception as e:
        return {"error": str(e)}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    """Obtiene un usuario por su ID"""
    user_service = UserService(Session)
    try:
        user = user_service.get_user_by_id(user_id)
        return user
    except Exception as e:
        return {"error": str(e)}

@app.post("/create_user")
def create_user(user_data: dict):
    """
    Crea un nuevo usuario
    Requiere: document_type_id, document_number, first_name, surname, email
    """
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


# =====================
# Bloque de peticiones de proveedor
# =====================
@app.get("/all_provider")
def all_provider():
    """Lista todos los proveedores"""
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.get_all_providers()
        return provider
    except Exception as e:
        return {"error" : str(e)}

@app.get("/provider/{provider_id}")
def get_provider_by_id(provider_id: int):
    """Obtiene un proveedor por su ID"""
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.get_provider_by_id(provider_id)
        return provider
    except Exception as e:
        return {"error" : str(e)}

@app.post("/create_provider")
def create_provider(provider_data: dict):
    """
    Crea un nuevo proveedor
    Requiere: name_provider
    """
    provider_service = ProviderService(Session)
    try:
        provider = provider_service.create_provider(
            provider_data["name_provider"]
        )
        return provider
    except Exception as e:
        return {"error" : str(e)}


# =====================
# Bloque de peticiones productos
# =====================
@app.get("/all_products")
def get_all_products():
    """Lista todos los productos"""
    product_service = ProductService(Session)
    try:
        products = product_service.get_all_products()
        return products
    except Exception as e:
        return {"error" : str(e)}

@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    """Obtiene un producto por su ID"""
    product_service = ProductService(Session)
    try:
        product = product_service.get_product_by_id(product_id)
        return product
    except Exception as e:
        return {"error" : str(e)}

@app.post("/create_product")
def create_product(product_data: dict):
    """
    Crea un nuevo producto
    Requiere: provider_id, category_id, name_product, quantity, isactive, price, image
    """
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
    
@app.post("/change_status_product")
def change_status_product(product_off: dict):
    """
    Cambia el estado de un producto
    Requiere: isactive, product_id
    """
    product_service = ProductService(Session)
    try:
        status_product_result = product_service.change_status_product(
            product_off["isactive"],
            product_off["product_id"]
        )
        return status_product_result
    except Exception as e:
        return {"error": str(e)}
@app.get("/get_products_category")
def get_products_by_category():
    """Lista todos los productos agrupados por categoría"""
    product_service = ProductService(Session)
    try:
        products = product_service.get_products_by_category()
        return products
    except Exception as e:
        return {"error": str(e)}
@app.get("/product_by_category/{category_id}")
def get_product_by_category(category_id: int):
    """Lista los productos de una categoría específica"""
    product_service = ProductService(Session)
    try:
        products = product_service.get_product_by_category(category_id)
        return products
    except Exception as e:
        return {"error": str(e)}


# =====================
# Bloque de peticiones de categorías
# =====================
@app.get("/categories")
def get_all_categories():
    """Lista todas las categorías disponibles"""
    category_service = CategoryService(Session)
    try:
        categories = category_service.get_all_category()
        return categories
    except Exception as e:
        return {"error": str(e)}

@app.get("/category/{category_id}")
def get_category(category_id: int):
    """Obtiene una categoría específica por su ID"""
    category_service = CategoryService(Session)
    try:
        category = category_service.get_category_by_id(category_id)
        return category
    except Exception as e:
        return {"error": str(e)}

@app.post("/create_category")
def create_category(category_data: dict):
    """
    Crea una nueva categoría
    Requiere: name
    Opcional: isactive (por defecto False)
    """
    category_service = CategoryService(Session)
    try:
        isactive = category_data.get("isactive", False)
        category = category_service.create_category(
            name=category_data["name"],
            isactive=isactive
        )
        return category
    except Exception as e:
        return {"error": str(e)}

@app.put("/category/{category_id}/status")
def change_category_status(category_id: int, status_data: dict):
    """
    Cambia el estado de una categoría
    Requiere: isactive (bool)
    """
    category_service = CategoryService(Session)
    try:
        category = category_service.change_status_category(
            category_id=category_id,
            isactive=status_data["isactive"]
        )
        return category
    except Exception as e:
        return {"error": str(e)}

# Configuración para Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
