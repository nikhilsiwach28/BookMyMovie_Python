from sqlalchemy import Column, Integer, String,ForeignKey
from ..Database.orm import Base

class Screen(Base):
    __tablename__ = 'screens'
    id = Column(Integer, primary_key=True)
    theatre_id = Column(Integer, ForeignKey('theatres.id'))
    seats = Column(Integer)