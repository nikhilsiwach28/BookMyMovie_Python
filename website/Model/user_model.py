# /bookmymovie/bookmymovie/database/user_model.py
from sqlalchemy import Column, Integer, String
from ..Database.orm import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    # Add other fields as needed
