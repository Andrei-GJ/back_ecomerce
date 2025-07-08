# services/user_service.py
from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.admin import Admin

class AdmintService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class
        
    def get_all_admins(self):
        session = self.Session()
        try:
            admin =  session.query(Admin).all()
            admin_dict = []
            for admin in admin:
                admin_dict.append({
                    'id': admin.id,
                    'iduser': admin.iduser,
                    'isactive':admin.isactive
                })
            return admin_dict
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()

    def get_add_by_id(self, admin_id: int):
        session = self.Session()
        try:
            admin = session.query(Admin).get(admin_id)
            return admin
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()

    def get_add_by_user_id(self, user_id:int):
        session = self.Session()
        try:
            admin = session.query(Admin).get(user_id)
            return admin
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()

    def change_status_admin(self, isactive: bool, admin_id: int):
        session = self.Session()
        try:
            admin = session.query(Admin).get(admin_id)
            if not admin:
                return {"error" : "No existe admin"}
            admin.isactive = isactive
            session.commit()
            return {
                'id': admin.id,
                'iduser': admin.iduser,
                'isactive':admin.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error" : str(e)}
        finally:
            session.close()

    def create_admin(self, iduser: int, isactive: bool):
        session = self.Session()
        try:
            new_admin = Admin (
                iduser = iduser,
                isactive = isactive
            )
            session.add(new_admin)
            session.commit()
            return {
                'id' : new_admin.id,
                'iduser': new_admin.iduser,
                'isactive' : new_admin.isactive
            }
        except Exception as e:
            session.rollback()
            return {"error" : str(e)}
        finally:
            session.close()