from fastapi import FastAPI
# from .routers import posts, users, auth, votes
# from .database import Base, engine

from fastapi.middleware.cors import CORSMiddleware
from database import base, engine
from . import auth_, regist

base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth_.router)
app.include_router(regist.router)
# app.include_router(users.router)
# app.include_router(votes.router)