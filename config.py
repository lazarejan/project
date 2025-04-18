from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_pass: str
    db_username: str
    db_hostname: str
    db_port: str
    db_name: str
    
    class Config:
        env_file = ".env"

settings = Settings()