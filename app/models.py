"""
    Defines SQLAlchemy ORM models
    Matches the finalized DB diagram exactly
"""

from sqlalchemy import Column,Integer,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

""" User Model """

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(255),unique=True,nullable=False)
    password=Column(String(255),nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.utcnow)