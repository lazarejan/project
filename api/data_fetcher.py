from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_session, Citizens, Account, Passport, ID_card, Car_license, Fine, Visa, BorderStamp
import schemas
from . import oauth_

router = APIRouter(
    prefix="/data_fetch",
    tags=["Data fetcher"]
)

@router.get("/passport", response_model=schemas.PassportGetBase)
def passport_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    pass_ = db.query(Passport).filter(Passport.personal_id == curr_user.personal_id).first()

    if not pass_:
        raise HTTPException(status_code=404, detail="Passport not found")
    
    return pass_

@router.get("/id_card", response_model=schemas.IDCardGetBase)
def id_card_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    id_card = db.query(ID_card).filter(ID_card.personal_id == curr_user.personal_id).first()

    if not id_card:
        raise HTTPException(status_code=404, detail="ID card not found")
    
    return id_card

@router.get("/car_license", response_model=schemas.CarLicenseGetBase)
def car_license_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    car_license = db.query(Car_license).filter(Car_license.personal_id == curr_user.personal_id).first()

    if not car_license:
        raise HTTPException(status_code=404, detail="Car license not found")
    
    return car_license

@router.get("/fine", response_model=list[schemas.FineGetBase])
def fine_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    fine = db.query(Fine).filter(Fine.personal_id == curr_user.personal_id).first()

    if not fine:
        raise HTTPException(status_code=404, detail="fine not found")
    
    return fine

@router.get("/visa", response_model=list[schemas.VisaGetBase])
def visa_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    visa = db.query(Visa).filter(Visa.personal_id == curr_user.personal_id).first()

    if not visa:
        raise HTTPException(status_code=404, detail="visa not found")
    
    return visa

@router.get("/borderstamp", response_model=list[schemas.BorderStampGetBase])
def borderstamp_get(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    borderstamp = db.query(BorderStamp).filter(BorderStamp.personal_id == curr_user.personal_id).first()

    if not borderstamp:
        raise HTTPException(status_code=404, detail="borderstamp not found")
    
    return borderstamp
