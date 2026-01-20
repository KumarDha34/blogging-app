"""
     ENtry point of the FAstAPi BLogging APplication
"""

from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routers import users,blogs,comments

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="FastAPI blogging Application",
    description="Simple Blogging with authentication, blogs and comments",
    version="1.0.0"
)

"""
Include routers

"""

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message":"FastAI Blogging Application is running"}