# services/user_service.py
from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.users import User

class UserService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class

    def create_user(self, document_type_id: int, document_number: str, first_name: str, surname: str, email: str):
        session = self.Session()
        try:
            new_user = User(
                documenttype = document_type_id,
                documentnumber = document_number,
                first_name = first_name,
                surname = surname,
                email = email
            )
            session.add(new_user)
            session.commit()
            return {
                'id': new_user.id,
                'documenttype': new_user.documenttype,
                'documentnumber': new_user.documentnumber,
                'first_name': new_user.first_name,
                'surname': new_user.surname,
                'email': new_user.email
            }
        except Exception as e:
            session.rollback()
            return {"error" : str(e)}
        finally:
            session.close()

    def get_user_by_id(self, user_id: int):
        session = self.Session()
        try:
            user = session.query(User).get(user_id)
            return user
        finally:
            session.close()

    def get_all_users(self):
        session = self.Session()
        try:
            users = session.query(User).all()
            users_dict = []
            for user in users:
                users_dict.append({
                    'id': user.id,
                    'documenttype': user.documenttype,
                    'documentnumber': user.documentnumber,
                    'first_name': user.first_name,
                    'surname': user.surname,
                    'email': user.email
                })
            return users_dict
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()