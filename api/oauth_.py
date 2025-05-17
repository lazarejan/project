from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordBearer
from database import get_session, Citizens, Account
from jose import JWTError, jwt
from datetime import timedelta, datetime

auth_schema = OAuth2PasswordBearer(tokenUrl='/login')

SECRET_KEY = "hello this is key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded

def verify_access_token(token, cred):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        # create acces token with username data
        id = payload.get("username")
        if not id:
            raise cred
    except JWTError:
        raise cred
    return id

def get_current_user(token: str = Depends(auth_schema), db: Session = Depends(get_session)):
    cred_exp= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="not authorized", headers= {"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token, cred_exp)
    # token is id now but later it will be schema so you have to use token.id'
    cur_user = db.query(Account).filter(Account.username == token).first()
    return cur_user
        