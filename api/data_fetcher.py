from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_session, Citizens, Account, Passport, ID_card, Car_license, Fine, Visa, BorderStamp
import schemas
from . import oauth_
from typing import Union

router = APIRouter(
    prefix="/data_fetch",
    tags=["Data fetcher"]
)

@router.get("/{doc_type}", response_model=Union[schemas.PassportGetBase, 
                                                schemas.IDCardGetBase, 
                                                schemas.CarLicenseGetBase, 
                                                list[schemas.FineGetBase], 
                                                list[schemas.VisaGetBase], 
                                                list[schemas.BorderStampGetBase]])
def data_fetch(doc_type: str, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    if doc_type == "passport":
        doc = db.query(Passport).filter(Passport.personal_id == curr_user.personal_id).first()
    elif doc_type == "id_card":
        doc = db.query(ID_card).filter(ID_card.personal_id == curr_user.personal_id).first()
    elif doc_type == "car_license":
        doc = db.query(Car_license).filter(Car_license.personal_id == curr_user.personal_id).first()
    elif doc_type == "fine":
        doc = db.query(Fine).filter(Fine.personal_id == curr_user.personal_id).all()
    elif doc_type == "visa":
        doc = db.query(Visa).filter(Visa.personal_id == curr_user.personal_id).all()
    elif doc_type == "borderstamp":
        doc = db.query(BorderStamp).filter(BorderStamp.personal_id == curr_user.personal_id).all()
    else:
        raise HTTPException(status_code=400, detail="Invalid document type")

    if not doc:
        raise HTTPException(status_code=404, detail=f"{doc_type} not found for the user")
    
    return doc