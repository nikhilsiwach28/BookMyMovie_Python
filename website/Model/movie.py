from sqlalchemy import Column, Integer, String
from ..Database.orm import Base

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    length = Column(Integer)
    genre = Column(String)