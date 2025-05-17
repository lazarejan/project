from pydantic_settings import BaseSettings
from pydantic import BaseModel

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