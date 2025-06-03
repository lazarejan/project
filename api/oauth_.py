from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordBearer
from database import get_session, Account
from jose import JWTError, jwt
from datetime import timedelta, datetime
import uuid

auth_schema = OAuth2PasswordBearer(tokenUrl='/login')

token_blacklist = set()

def blacklist_token(jti: str):
    token_blacklist.add(jti)

def is_token_blacklisted(jti: str) -> bool:
    return jti in token_blacklist

SECRET_KEY = "hello this is key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "jti": str(uuid.uuid4())})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded

def verify_access_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        # create acces token with username data
        jti = payload.get("jti")
        if jti and is_token_blacklisted(jti):
            raise HTTPException(status_code=401, detail="Token has been revoked")
        return id
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized", headers= {"WWW-Authenticate": "Bearer"})

def logout(token: str = Depends(auth_schema)):
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        jti = payload.get("jti")
        if jti:
            blacklist_token(jti)
        return {"msg": "Logged out successfully"}
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")

def get_current_user(token: str = Depends(auth_schema), db: Session = Depends(get_session)):
    token = verify_access_token(token)
    cur_user = db.query(Account).filter(Account.username == token).first()
    return cur_user