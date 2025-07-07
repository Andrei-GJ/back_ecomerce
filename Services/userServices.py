# services/user_service.py
from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.users import User  # Asegúrate que el archivo se llama 'user.py'

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
            print(f"Usuario '{first_name} {surname}' creado con ID: {new_user.id}")
            return new_user
        except Exception as e:
            session.rollback()
            print(f"Error al crear usuario '{first_name} {surname}': {e}")
            return None
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
        finally:
            session.close()