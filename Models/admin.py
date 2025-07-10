from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from Models.base import Base

class Admin(Base):
    __tablename__ = 'admin'
    
    # Columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    iduser = Column(Integer, ForeignKey('users.id'), nullable=True)
    isactive = Column(Boolean, default=True, nullable=True)
    
    # Relaciones (opcionales, dependiendo de tus otros modelos)
    user = relationship("User", back_populates="admin")
    
    def __repr__(self):
        return f"<Admin(id={self.id}, iduser={self.iduser}, isactive={self.isactive})>"
    
    def __str__(self):
        return f"Admin {self.id} - User: {self.iduser}"