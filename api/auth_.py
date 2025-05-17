from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from database import get_session, Citizens, Account
import oauth
from . import oauth_

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(user_info: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    user = db.query(Account).filter(Account.username == user_info.username).first()
    print(oauth.decrypt(user.password) != user_info.password, oauth.decrypt(user_info.password), user_info.password)
    if not user or oauth.decrypt(user.password) != user_info.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "user not found")
    
    access_token = oauth_.create_access_token({"username": user_info.username})
    return {"token": access_token}
