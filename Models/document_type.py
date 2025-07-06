from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from Models.base import Base

class DocumentType(Base):
    __tablename__ = 'document_type'
    
    # Columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=True)
    code = Column(Numeric(3), nullable=True)
    
    # Relaciones
    users = relationship("User", back_populates="document_type")
    
    def __repr__(self):
        return f"<DocumentType(id={self.id}, name='{self.name}', code={self.code})>"
    
    def __str__(self):
        return f"{self.name} ({self.code})" if self.name else f"DocumentType {self.id}"