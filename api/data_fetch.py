from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Car, Citizens, get_session, Fine, Visa, BorderStamp
import schemas
from . import oauth_
from typing import Union, List

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

@router.get("/search", response_model=List[schemas.PersonBase])
def user_search(db: Session = Depends(get_session), search: str = ""):

    user_w_id = db.query(Citizens).filter(Citizens.personal_id.like(f"{search}%")).all()
    user_w_name = db.query(Citizens).filter(Citizens.first_name.like(f"{search}%")).all()
    user_w_lname = db.query(Citizens).filter(Citizens.last_name.like(f"{search}%")).all()

    res = user_w_id+user_w_name+user_w_lname

    if res == []:
        raise HTTPException(status_code=404, detail="Users not found")

    return user_w_id+user_w_name+user_w_lname

@router.get("/{doc_type}", response_model=Union[list[schemas.FineGetBase], 
                                                list[schemas.VisaGetBase], 
                                                list[schemas.BorderStampGetBase],
                                                list[schemas.CarBase]])
def user_data(doc_type: str, db: Session = Depends(get_session), curr_user: Session = Depends(oauth_.get_current_user)):
    match doc_type:
        case "fine":
            doc = db.query(Fine).filter(Fine.personal_id == curr_user.personal_id).all()
        case "visa":
            doc = db.query(Visa).filter(Visa.personal_id == curr_user.personal_id).all()
        case "borderstamp":
            doc = db.query(BorderStamp).filter(BorderStamp.personal_id == curr_user.personal_id).all()
        case "car":
            doc = db.query(Car).filter(Car.owner == curr_user.personal_id).all()
        case _:
            raise HTTPException(status_code=400, detail="Invalid document type")
    
    if not doc:
        raise HTTPException(status_code=404, detail=f"{doc_type} not found for the user")
    
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