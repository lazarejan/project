from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATE, Integer, Enum
import enum
from config import settings

URL = f'postgresql://{settings.db_username}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}'

engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine)

def get_session(func):
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            result = func(*args, **kwargs, db=session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    return wrapper

base = declarative_base()

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"

class Citizens(base):
    __tablename__ = "citizens"

    personal_id = Column(String(11), primary_key=True, nullable=False) 
    first_name = Column(String, nullable=False) 
    last_name = Column(String, nullable=False) 
    birth_date = Column(DATE, nullable=False) 
    sex = Column(Enum(GenderEnum), nullable=False) 
    address = Column(String, nullable=False) 

class Account(base):
    __tablename__ = "account"
    
    username = Column(String, unique=True, nullable=False, primary_key=True)
    password = Column(String, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)

class ID_card(base):
    __tablename__ = "ID_card"

    card_id = Column(String(9), nullable=False, unique=True, primary_key=True)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)

class Passport(base):
    __tablename__ = "passport"

    id = Column(Integer, primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    
class Car_license(base):
    __tablename__ = "carlicense"
    
    id = Column(Integer, primary_key=True)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)

base.metadata.create_all(bind=engine)

