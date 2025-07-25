# services/user_service.py
from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.category import Category

class CategoryService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class
    
    def get_all_category(self):
        session = self.Session()
        try:
            category = session.query(Category).all()
            category_dic = []
            for category in category:
                category_dic.append({
                    'id':category.id,
                    'name':category.name,
                    'isactive':category.isactive
                })
            return category_dic
        except Exception as e:
            return {"error": str(e)}
        finally:
            session.close()

    def get_category_by_id(self , category_id:int):
        session = self.Session()
        try:
            category_id = session.query(Category).get (category_id)
            return category_id
        except Exception as e:
            return {"error": str(e)}
        finally:
            session.close()

    def change_status_category(self , category_id: int , isactive : bool):
        session = self.Session()
        try:
            category = session.query(Category).get (category_id)
            category.isactive = isactive
            session.commit()
            return {
                'id':category.id,
                'name':category.name,
                'isactive':category.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        finally:
            session.close()\

    def create_category(self, name: str, isactive: bool = False):
        session = self.Session()
        try:
            new_category = Category(
                name=name,
                isactive=isactive
            )
            session.add(new_category)
            session.commit()
            return {
                'id': new_category.id,
                'name': new_category.name,
                'isactive': new_category.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        finally:
            session.close()