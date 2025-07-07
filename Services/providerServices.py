# services/user_service.py
from sqlalchemy.orm import sessionmaker
# Importa tu modelo User desde su ubicación
from Models.provider import Provider 

class ProviderService:
    def __init__(self, Session_class: sessionmaker):
        """Inicializa el servicio con una clase de sesión de SQLAlchemy."""
        self.Session = Session_class
    
    def get_all_providers(self):
        session = self.Session()
        try:
            providers = session.query(Provider).all()
            provider_dic = []
            for provider in providers:
                provider_dic.append({
                    'id' : provider.id,
                    'name_provider' : provider.name_provider
                })
            return provider_dic
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()
    
    def get_provider_by_id(self , provider_id: int):
        session = self.Session()
        try:
            provider = session.query(Provider).get(provider_id)
            return provider
        except Exception as e:
            return {"error" : str(e)}
        finally:
            session.close()

    def create_provider (self, name_provider):
        session = self.Session()
        try:
            new_provider = Provider (
                name_provider = name_provider
            )
            session.add(new_provider)
            session.commit()
            return {
                new_provider.name_provider,
                new_provider.id
            }
        except Exception as e:
            session.rollback()
            return {"error" : str(e)}
        finally:
            session.close()