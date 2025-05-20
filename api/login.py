from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from database import get_session, Account
import hash
import schemas
from . import oauth_

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("", response_model=schemas.TokenBase)
def login(user_info: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    user = db.query(Account).filter(Account.username == user_info.username).first()

    if not user or hash.decrypt(user.password) != user_info.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "user not found")
    
    access_token = oauth_.create_access_token({"username": user_info.username})
    return {"token": access_token}
