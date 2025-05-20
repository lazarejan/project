from fastapi import FastAPI
from . import regist, data_fetcher, login

app = FastAPI()

app.include_router(login.router)
app.include_router(regist.router)
app.include_router(data_fetcher.router)