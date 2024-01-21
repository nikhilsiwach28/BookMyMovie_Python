# /bookmymovie/bookmymovie/database/orm.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL ="postgresql://new_admin_user:your_password@localhost:5432/bookmyshow"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
