from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from Models.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    documenttype = Column(Integer, ForeignKey('document_type.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    documentnumber = Column(String(20), nullable=True)
    first_name = Column(String(50), nullable=True)
    surname = Column(String(50), nullable=True)
    email = Column(String(40), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.first_name} {self.surname}', email='{self.email}')>"

    def __str__(self):
        return f"{self.first_name} {self.surname} <{self.email}>"
