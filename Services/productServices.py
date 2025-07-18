# services/user_service.py
from itertools import product

from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.product import Product

class ProductService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class

    def get_all_products(self):
        session = self.Session()
        try:
            products = session.query(Product).all()
            products_dict = []
            for product in products:
                products_dict.append({
                    'id': product.id,
                    'name_product': product.name_product,
                    'price': product.price,
                    'category_id': product.category_id,
                    'isactive': product.isactive
                })
            return products_dict
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()
            
    def get_product_by_id(self , product_id: int):
        session = self.Session()
        try:
            product = session.query(Product).get(product_id)
            return product
        except Exception as e:
            return {"error": str(e)}
        finally:
            session.close()

    def create_product(self, provider_id: int, category_id: int, name_product: str, quantity: int, isactive: bool, price: int, image: str):
        session = self.Session()
        try:
            new_product = Product(
                category_id=category_id,
                provider_id=provider_id,
                name_product=name_product,
                quantity=quantity,
                isactive=isactive,
                price=price,
                image=image
            )
            session.add(new_product)
            session.commit()
            return {
                'id': new_product.id,
                'name_product': new_product.name_product,
                'price': new_product.price,
                'category_id': new_product.category_id,
                'provider_id': new_product.provider_id,
                'isactive': new_product.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        finally:
            session.close()

    def change_status_product(self, isactive: bool, product_id: int):
        session = self.Session()
        try:
            product = session.query(Product).get(product_id)
            if not product:
                return {"error": "Producto no encontrado"}
            product.isactive = isactive
            session.commit()
            return {
                "id": product.id,
                "name_product": product.name_product,
                "isactive": product.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        finally:
            session.close()

    def get_product_by_category(self , category_id:int ):
        session = self.Session()
        try:
            products = session.query(Product).filter(Product.category_id == category_id).all()
            products_dict = []
            for product in products:
                products_dict.append({
                    'id': product.id,
                    'name_product': product.name_product,
                    'price': product.price,
                    'category_id': product.category_id,
                    'isactive': product.isactive
                })
            return products_dict
        except Exception as e:
            return {"error": str(e)}
        finally:
            session.close()

    def get_products_by_category(self):
        session = self.Session()
        try:
            from Models.category import Category
            categories = session.query(Category).all()
            result = []
            for category in categories:
                products = [
                    {
                        'id': p.id,
                        'name_product': p.name_product,
                        'price': p.price,
                        'isactive': p.isactive,
                        'provider_id': p.provider_id
                    }
                    for p in category.products
                ]
                result.append({
                    'category_id': category.id,
                    'category_name': getattr(category, 'name_category', None),
                    'products': products
                })
            return result
        except Exception as e:
            return {'error': str(e)}
        finally:
            session.close()
