from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from Models.base import Base

class Product(Base):
    __tablename__ = 'products'
    
    # Columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    provider_id = Column(Integer, ForeignKey('provider.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    name = Column(String(50), nullable=False)
    quantity = Column(Integer, default=0, nullable=True)
    isactive = Column(Boolean, default=False, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    image = Column(String(300), nullable=True)
    
    # Constraint para cantidad no negativa
    __table_args__ = (
        CheckConstraint('quantity >= 0', name='products_quantity_check'),
    )
    
    # Relaciones (opcionales, dependiendo de tus otros modelos)
    provider = relationship("Provider", back_populates="products")
    category = relationship("Category", back_populates="products")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
    
    def __str__(self):
        return f"{self.name} - ${self.price}"