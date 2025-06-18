from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Car, Citizens, get_session, Passport, ID_card, Car_license, Fine, Visa, BorderStamp
import schemas
from . import oauth_
from typing import Union

router = APIRouter(
    prefix="/data_fetch",
    tags=["Data fetcher"]
)

@router.get("", response_model=schemas.UserInfoGetBase)
def user(db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    citizen = db.query(Citizens).filter(
        Citizens.personal_id == curr_user.personal_id
    ).first()
    
    if not citizen:
        raise HTTPException(status_code=404, detail="User not found")
    
    return citizen

@router.get("/{doc_type}", response_model=Union[schemas.PassportGetBase, 
                                                schemas.IDCardGetBase, 
                                                schemas.CarLicenseGetBase, 
                                                list[schemas.FineGetBase], 
                                                list[schemas.VisaGetBase], 
                                                list[schemas.BorderStampGetBase],
                                                list[schemas.CarBase]])
def user_data(doc_type: str, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
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
    elif doc_type == "car":
        doc = db.query(Car).filter(Car.owner == curr_user.personal_id).all()
    else:
        raise HTTPException(status_code=400, detail="Invalid document type")
    
    if not doc:
        raise HTTPException(status_code=404, detail=f"{doc_type} not found for the user")
    
    return doc

@router.get("/search/{doc_type}", response_model=Union[list[schemas.FineGetBase], 
                                                list[schemas.VisaGetBase], 
                                                list[schemas.BorderStampGetBase]])
def search_data(doc_type: str, db: Session = Depends(get_session), search: str = "", search_type: str = "", order_by: str = "", sort: str = "asc"):
    docs = {"visa": Visa, "borderstamp": BorderStamp, "fine": Fine}
    
    match doc_type:
        case "visa":
            doc_query = db.query(Visa)
        case "borderstamp":
            doc_query = db.query(BorderStamp)
        case "fine":
            doc_query = db.query(Fine)
        case _:
            raise HTTPException(status_code=400, detail="Invalid document type")
    
    if search_type:
        match search_type:
            case "personal_id":
                doc_query = doc_query.filter(docs[doc_type].personal_id.like(f"{search}%"))
            case "type":
                doc_query = doc_query.filter(docs[doc_type].type == search)
            case "status":
                doc_query = doc_query.filter(docs[doc_type].status == search)
            case "country":
                doc_query = doc_query.filter(docs[doc_type].country == search)
            case _:
                raise HTTPException(status_code=400, detail="Invalid search type")
        
    if order_by:
        match order_by, sort:
            case "issue_date", "desc":
                doc_query = doc_query.order_by(docs[doc_type].issue_date.desc())
            case "issue_date", "asc":
                doc_query = doc_query.order_by(docs[doc_type].issue_date.asc())
            case "expiration_date", "desc":
                doc_query = doc_query.order_by(docs[doc_type].expiration_date.desc())
            case "expiration_date", "asc":
                doc_query = doc_query.order_by(docs[doc_type].expiration_date.asc())
            case "amount", "desc":
                doc_query = doc_query.order_by(docs[doc_type].amount.desc())
            case "amount", "asc":
                doc_query = doc_query.order_by(docs[doc_type].amount.asc())
            case _:
                raise HTTPException(status_code=400, detail="Invalid order by or sort type")
        
    doc = doc_query.all()
    
    return doc

@router.put("/update_fine_status/{doc_id}", response_model=schemas.FineGetBase)
def upd_fine(doc_id: int, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    
    fine_query = db.query(Fine).filter(Fine.fine_id == doc_id)
    fine = fine_query.first()

    if not fine:
        raise HTTPException(status_code=404, detail="Fine not found")
    fine.status = "გადახდილი"

    db.commit()
    db.refresh(fine)
    return fine