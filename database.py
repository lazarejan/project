from sqlalchemy import CheckConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATE, Integer

URL = "sqlite:///mydatabase.db"

engine = create_engine(URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

base = declarative_base()

class Citizens(base):
    __tablename__ = "citizens"

    personal_id = Column(String(11), primary_key=True, nullable=False) 
    first_name = Column(String, nullable=False) 
    last_name = Column(String, nullable=False) 
    birth_date = Column(DATE, nullable=False) 
    sex = Column(String, nullable=False) 
    address = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("sex in ('მმ', 'მდ')", name="check_sex"),
    )

class Account(base):
    __tablename__ = "account"
    
    username = Column(String, unique=True, nullable=False, primary_key=True)
    password = Column(String, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)

class ID_card(base):
    __tablename__ = "id_card"

    card_id = Column(String(9), nullable=False, primary_key=True)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)

class Passport(base):
    __tablename__ = "passport"

    passport_id = Column(String(9), primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    
class Car_license(base):
    __tablename__ = "car_license"
    
    car_license_id = Column(String(9), primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)

class Fine(base):
    __tablename__ = "fine"

    fine_id = Column(Integer, primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False, server_default="unpaid")

    __table_args__ = (
        CheckConstraint("type IN ('administrative', 'vehicle', 'other')", name="check_type"),
        CheckConstraint("status IN ('paid', 'unpaid', 'expired')", name="check_status")
    )

class Visa(base):
    __tablename__ = "visa"

    visa_id = Column(Integer, primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    passport_id = Column(String(9), ForeignKey("passport.passport_id"), nullable=False)
    country = Column(String, nullable=False)
    type = Column(String, nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)

    __table_args__ = (
        CheckConstraint("type IN ('tourist', 'business', 'student', 'work', 'family')", name="check_type"),
    )

class BorderStamp(base):
    __tablename__ = "borderstamp"

    stamp_id = Column(Integer, primary_key=True)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    passport_id = Column(String(9), ForeignKey("passport.passport_id"), nullable=False)
    timestamp = Column(DATE, nullable=False)
    location = Column(String, nullable=False)
    direction = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint("direction IN ('entry', 'exit')", name="check_direction"),
    )

base.metadata.create_all(bind=engine)

