# services/user_service.py
from sqlalchemy.orm import sessionmaker
from Models.users import User
import hashlib

class UserService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, email: str, password: str, first_name: str, surname: str, document_type_id: int, document_number: str):
        session = self.Session()
        try:
            # Verificar si el usuario ya existe
            existing_user = session.query(User).filter(User.email == email).first()
            if existing_user:
                return {"error": "El email ya está registrado"}
            
            # Crear nuevo usuario
            hashed_password = self.hash_password(password)
            new_user = User(
                documenttype=document_type_id,
                documentnumber=document_number,
                first_name=first_name,
                surname=surname,
                email=email,
                password=hashed_password
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
            return {"error": str(e)}
        finally:
            session.close()

    def login(self, email: str, password: str):
        session = self.Session()
        try:
            hashed_password = self.hash_password(password)
            user = session.query(User).filter(
                User.email == email,
                User.password == hashed_password
            ).first()
            
            if not user:
                return {"error": "Email o contraseña incorrectos"}
            
            return {
                'id': user.id,
                'documenttype': user.documenttype,
                'documentnumber': user.documentnumber,
                'first_name': user.first_name,
                'surname': user.surname,
                'email': user.email
            }
        except Exception as e:
            return {"error": str(e)}
        finally:
            session.close()

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