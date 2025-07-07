from sqlalchemy import Column, Integer, String
from Models.base import Base

class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_provider = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"<Provider(id={self.id}, name_provider='{self.name_provider}')>"