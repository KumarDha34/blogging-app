"""
    Handles database connection and session management
    for POSTGRESQL using SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


"""Load environment variables from .env files"""

load_dotenv()


"""Database URL from environmemt"""
DATABASE_URL=os.getenv("DATABASE_URL")

""" Creat SQLAchemy engine """
engine=create_engine(DATABASE_URL)


""" Create Session """
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

""" Base class for models"""
Base=declarative_base()



""" dependency to get DB session """
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()