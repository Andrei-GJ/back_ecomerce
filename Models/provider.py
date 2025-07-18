from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base

class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_provider = Column(String(50), nullable=True)
    # Add relationship to Product
    products = relationship("Product", back_populates="provider")

    def __repr__(self):
        return f"<Provider(id={self.id}, name_provider='{self.name_provider}')>"