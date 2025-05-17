from fastapi import FastAPI
# from .routers import posts, users, auth, votes
# from .database import Base, engine

from . import auth_, regist, data_fetcher

app = FastAPI()


app.include_router(auth_.router)
app.include_router(regist.router)
app.include_router(data_fetcher.router)
# app.include_router(users.router)
# app.include_router(votes.router)