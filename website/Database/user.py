# /bookmymovie/bookmymovie/database/user_orm.py
from .orm import SessionLocal
from ..Model.user_model import User

def getUserFromDb(phone: int):
    session = SessionLocal()
    return session.query(User).filter(User.phone == phone).first()
