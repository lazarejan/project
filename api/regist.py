from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_session, Citizens, Account
import hash 
from . import oauth_
import schemas

router = APIRouter(
    prefix="/register",
    tags=["Registration"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.TokenBase)
def register(user_info: schemas.UserRegister, db: Session = Depends(get_session)):
    citizen = db.query(Citizens).filter(Citizens.personal_id == user_info.pers_id).first()
    is_registered = db.query(Account).filter(Account.personal_id == user_info.pers_id).first()
    username_taken = db.query(Account).filter(Account.username == user_info.username).first()
    # is_email = db.query(Account).filter(Account.email == user_info.email).first()

    if is_registered:
        raise HTTPException(status_code=400, detail="User already registered")

    if username_taken:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    if not citizen:
        raise HTTPException(status_code=400, detail="Citizen not found")
    
    # if is_email:
    #     raise HTTPException(status_code=400, detail="Email already registered")

    user_info.password = hash.encrypt(user_info.password)

    add_account = Account(username=user_info.username, password=user_info.password, personal_id=citizen.personal_id)
    db.add(add_account)
    db.commit()
    access_token = oauth_.create_access_token({"username": user_info.username})
    return {"token": access_token}