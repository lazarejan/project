from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import Car, Citizens, Passport, Visa, get_session, Fine, BorderStamp
from datetime import date, timedelta
from . import oauth_
import schemas

# these requests are for special users (police, border guard etc)
# last step: dont forget to add curr_user checker so that it checks whether request is sent from special_user or not

router = APIRouter(
    tags=["Update User Information"]
)

@router.post("/fine", response_model=schemas.FineGetBase)
def post_fine(fine_info: schemas.FinePostBase, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    fine_info = fine_info.dict()
    fine_info["issue_date"] = date.today()
    fine_info["expiration_date"] = date.today() + timedelta(days=fine_info["duration_days"])

    del fine_info["duration_days"]

    add_fine = Fine(**fine_info)
    db.add(add_fine)
    db.commit()
    db.refresh(add_fine)
    return add_fine

@router.post("/visa", response_model=schemas.VisaGetBase)
def post_visa(visa_info: schemas.VisaPostBase, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    visa_info = visa_info.dict()
    visa_info["passport_id"] = db.query(Passport).join(Citizens, Citizens.personal_id == Passport.personal_id).group_by(Passport.personal_id).first().passport_id
    visa_info["issue_date"] = date.today()
    visa_info["expiration_date"] = date.today() + timedelta(days=365*visa_info["duration_years"])
    
    del visa_info["duration_years"]
    
    add_visa = Visa(**visa_info)
    db.add(add_visa)
    db.commit()
    db.refresh(add_visa)
    return add_visa

@router.post("/borderstamp", response_model=schemas.BorderStampGetBase)
def post_borderstamp(borderstamp_info: schemas.BorderStampPostBase, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    borderstamp_info = borderstamp_info.dict()
    borderstamp_info["timestamp"] = date.today()
    borderstamp_info["passport_id"] = db.query(Passport).join(Citizens, Citizens.personal_id == Passport.personal_id).group_by(Passport.personal_id).first().passport_id

    add_borderstamp = BorderStamp(**borderstamp_info)
    db.add(add_borderstamp)
    db.commit()
    db.refresh(add_borderstamp)
    return add_borderstamp

@router.post("/car", response_model=schemas.CarBase)
def post_car(car_info: schemas.CarBase, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    car_info = car_info.dict()
    is_car_id = db.query(Car).filter(Car.car_id == car_info["car_id"]).first()

    if is_car_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="car id already exists")    

    add_car = Car(**car_info)
    db.add(add_car)
    db.commit()
    db.refresh(add_car)
    return add_car