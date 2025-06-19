from fastapi import FastAPI
from . import regist, login, special_req, user_req
from fastapi_utils.tasks import repeat_every
from database import  Car_license, ID_card, Passport, SessionLocal, Fine, Visa
from datetime import date

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=60*60*24)  # 24 hours
def check_fine_expire():
    db = SessionLocal()
    today = date.today()
    exp_fines = db.query(Fine).filter(Fine.expiration_date < today, Fine.status == "გადასახდელი").all()

    for docs in (ID_card, Passport, Car_license, Visa):
        exp_docs = db.query(docs).filter(
        docs.expiration_date < today,
        docs.status == "აქტიური"
        ).all()
        for doc in exp_docs:
            doc.status = "გაუქმებული"

    for fine in exp_fines:
        fine.status = "ვადაგასული"
        fine.amount += 50
        fine.message += "!!! jarimas vada gauvida oqroo (+50 GEL) !!!"

    db.commit()
    db.close()

app.include_router(login.router)
app.include_router(regist.router)
app.include_router(user_req.router)
app.include_router(special_req.router)