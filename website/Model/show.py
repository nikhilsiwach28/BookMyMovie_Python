from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Float
from ..Database.orm import Base

class Show(Base):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    theatre_id = Column(Integer, ForeignKey('theatres.id'))
    date_time = Column(DateTime)
    screen_id = Column(Integer, ForeignKey('screens.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    price = Column(Float)