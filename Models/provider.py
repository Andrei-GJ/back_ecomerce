from sqlalchemy import Column, Integer, String
from Models.base import Base

class Provider(Base):
    __tablename__ = 'provider'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    # Puedes agregar más campos según tu necesidad

    def __repr__(self):
        return f"<Provider(id={self.id}, name='{self.name}')>"
