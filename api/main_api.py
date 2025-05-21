from fastapi import FastAPI
from . import regist, data_fetcher, login, user_info
from fastapi_utils.tasks import repeat_every
from database import SessionLocal, Fine
from datetime import date

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=60*60*24)  # 24 hours
def check_fine_expire():
    db = SessionLocal()
    today = date.today()
    fines = db.query(Fine).filter(Fine.expiration_date < today, Fine.status == "unpaid").all()
    for fine in fines:
        fine.status = "expired"
    print("Expiration check")
    db.commit()
    db.close()

app.include_router(login.router)
app.include_router(regist.router)
app.include_router(data_fetcher.router)
app.include_router(user_info.router)