from pydantic_settings import BaseSettings
from pydantic import BaseModel, validator
import re
from datetime import date

class Settings(BaseSettings):
    db_pass: str
    db_username: str
    db_host: str
    db_port: str
    db_name: str
    
    class Config:
        env_file = ".env"

settings = Settings()

class UserRegister(BaseModel):
    pers_id: str
    username: str
    password: str
    r_password: str

    @validator('password')
    def validate_password(cls, password):
        if 8 > len(password)  or len(password) > 20:
            raise ValueError("Password must bebetween 8 and 20")
        
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter")
            
        if not re.search(r'[a-z]', password):
            raise ValueError("Password must contain at least one lowercase letter")
            
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one digit")
            
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError("Password must contain at least one special character")
        return password
    
    @validator("username")
    def validate_username(cls, username):
        if len(username) < 5 or len(username) > 20:
            raise ValueError("passwrod must contain at least one lowercase letter")

        if not re.search(r'[a-z]', username):
            raise ValueError("Password must contain at least one lowercase letter")


class IDCardGetBase(BaseModel):
    card_id: str
    personal_id: str
    issue_date: date
    expiration_date: date

class PassportGetBase(BaseModel):
    passport_id: str
    personal_id: str
    issue_date: date
    expiration_date: date

class CarLicenseGetBase(BaseModel):
    car_license: str
    personal_id: str
    issue_date: date
    expiration_date: date

class FineGetBase(BaseModel):
    fine_id: int
    personal_id: str
    type: str
    message: str
    issue_date: date
    expiration_date: date
    amount: int
    status: str

class VisaGetBase(BaseModel):
    visa_id: int
    passport_id: str
    country: str
    type: str
    issue_date: date
    expiration_date: date

class BorderStampGetBase(BaseModel):
    stamp_id: int
    passport_id: str
    timestamp: date
    location: str
    direction: str

class TokenBase(BaseModel):
    token: str