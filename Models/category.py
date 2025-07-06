from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from Models.base import Base

class Category(Base):
    __tablename__ = 'category'
    
    # Columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    isactive = Column(Boolean, default=False, nullable=True)
    
    # Relaciones (opcionales, dependiendo de tus otros modelos)
    # products = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', isactive={self.isactive})>"
    
    def __str__(self):
        return f"{self.name}" if self.name else f"Category {self.id}"