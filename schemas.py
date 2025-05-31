from fastapi import HTTPException
from pydantic import BaseModel, validator, model_validator
from datetime import date
import re

from database import Car_license

class UserRegister(BaseModel):
    pers_id: str
    username: str
    password: str
    r_password: str

    @validator('password')
    def validate_password(cls, password):
        errors = []
        
        if len(password) < 8 or len(password) > 20:
            errors.append("Password must be between 8 and 20 characters")
        
        if not re.search(r'[A-Z]', password):
            errors.append("Password must contain at least one uppercase letter")
            
        if not re.search(r'[a-z]', password):
            errors.append("Password must contain at least one lowercase letter")
            
        if not re.search(r'[0-9]', password):
            errors.append("Password must contain at least one digit")
            
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain at least one special character")

        if errors:
            raise HTTPException(status_code=400, detail="\n".join(errors))
        return password
    
    @validator("username")
    def validate_username(cls, username):
        errors = []
        
        if len(username) < 5 or len(username) > 20:
            errors.append("Username must be between 5 and 20 characters")

        if not re.search(r'[a-z]', username):
            errors.append("Username must contain at least one lowercase letter")
            
        if errors:
            raise HTTPException(status_code=400, detail="\n".join(errors))
        return username
    
    @model_validator(mode='after')
    def passwords_match(self):
        if self.password != self.r_password:
            raise HTTPException(status_code=400, detail='Password and repeated password must be the same')
        return self

class IDCardGetBase(BaseModel):
    card_id: str
    personal_id: str
    issue_date: date
    expiration_date: date

    class Config:
        from_attributes = True

class PassportGetBase(BaseModel):
    passport_id: str
    personal_id: str
    issue_date: date
    expiration_date: date
    
    class Config:
        from_attributes = True

class CarLicenseGetBase(BaseModel):
    car_license_id: str
    personal_id: str
    issue_date: date
    expiration_date: date
    
    class Config:
        from_attributes = True

class FineGetBase(BaseModel):
    fine_id: int
    personal_id: str
    type: str
    message: str
    issue_date: date
    expiration_date: date
    amount: int
    status: str

class FinePostBase(BaseModel):
    personal_id: str
    type: str
    message: str
    amount: int
    status: str = "unpaid"

class VisaGetBase(BaseModel):
    visa_id: int
    personal_id: str
    passport_id: str
    country: str
    type: str
    issue_date: date
    expiration_date: date

class VisaPostBase(BaseModel):
    personal_id: str
    country: str
    type: str
    duration_years: int

class BorderStampGetBase(BaseModel):
    stamp_id: int
    personal_id: str
    passport_id: str
    timestamp: date
    location: str
    direction: str

class BorderStampPostBase(BaseModel):
    personal_id: str
    location: str
    direction: str

class UserInfoGetBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    sex: str
    address: str
    id_card: IDCardGetBase
    passport: PassportGetBase
    car_license: CarLicenseGetBase
    
    class Config:
        from_attributes = True
        
class TokenBase(BaseModel):
    token: str