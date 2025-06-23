from fastapi import FastAPI
from . import data_fetch, data_upd, regist, login
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
        fine.amount += 100
        fine.message += "!!! ჯარიმას ვადა გაუვიდა ოქრო (+100 GEL) !!!"

    db.commit()
    db.close()

app.include_router(login.router)
app.include_router(regist.router)
app.include_router(data_fetch.router)
app.include_router(data_upd.router)