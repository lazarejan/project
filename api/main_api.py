from fastapi import FastAPI
from . import regist, login, special_req, user_req
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
        fine.amount += 50
    print("Expiration check")
    db.commit()
    db.close()

app.include_router(login.router)
app.include_router(regist.router)
app.include_router(user_req.router)
app.include_router(special_req.router)