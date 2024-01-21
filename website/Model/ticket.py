from sqlalchemy import Column, Integer, String,ForeignKey
from ..Database.orm import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    show_id = Column(Integer, ForeignKey('shows.id'))
    number_of_tickets = Column(Integer)
    # Add other fields as needed