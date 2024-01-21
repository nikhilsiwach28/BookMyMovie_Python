from sqlalchemy import Column, Integer, String, ForeignKey
from ..Database.orm import Base

class Theatre(Base):
    __tablename__ = 'theatres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = Column(String)
    # Add other fields as needed