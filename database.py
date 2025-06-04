from sqlalchemy import CheckConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DATE, Integer, String

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
    sex = Column(String(2), nullable=False) 
    address = Column(String, nullable=False)

    id_card = relationship("ID_card", uselist=False)
    passport = relationship("Passport", uselist=False)
    car_license = relationship("Car_license", uselist=False)

    __table_args__ = (
        CheckConstraint("sex in ('მმ', 'მდ', '-')", name="check_sex"),
    )

class Account(base):
    __tablename__ = "account"
    
    username = Column(String, unique=True, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)

class ID_card(base):
    __tablename__ = "id_card"

    card_id = Column(String(9), nullable=False, primary_key=True)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    status = Column(String, nullable=False, server_default="აქტიური")

    __table_args__ = (
        CheckConstraint("status in ('აქტიური', 'გაუქმებული')", name="status_check"),
    )

class Passport(base):
    __tablename__ = "passport"

    passport_id = Column(String(9), primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    status = Column(String, nullable=False, server_default="აქტიური")

    __table_args__ = (
        CheckConstraint("status in ('აქტიური', 'გაუქმებული')", name="status_check"),
    )
    
class Car_license(base):
    __tablename__ = "car_license"
    
    car_license_id = Column(String(9), primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    status = Column(String, nullable=False, server_default="აქტიური")

    __table_args__ = (
        CheckConstraint("status in ('აქტიური', 'გაუქმებული')", name="status_check"),
    )

class Car(base):
    __tablename__ = "car"

    car_id = Column(String, primary_key=True, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    owner = Column(String(9), ForeignKey("citizens.personal_id"), nullable=False)

class Fine(base):
    __tablename__ = "fine"

    fine_id = Column(Integer, primary_key=True, nullable=False)
    personal_id = Column(String(11), ForeignKey("citizens.personal_id"), nullable=False)
    type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    issue_date = Column(DATE, nullable=False)
    expiration_date = Column(DATE, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String, nullable=False, server_default="გადასახდელი")

    __table_args__ = (
        CheckConstraint("type IN ('ადმინისტრაციული', 'საგზაო', 'სხვა')", name="check_type"),
        CheckConstraint("status IN ('გადახდილი', 'გადასახდელი', 'ვადაგასული')", name="check_status")
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
    status = Column(String, nullable=False, server_default="აქტიური")

    __table_args__ = (
        CheckConstraint("status in ('აქტიური', 'გაუქმებული')", name="status_check"),
        CheckConstraint("type IN ('ტურისტული', 'ბიზნეს', 'სტუდენტური', 'სამუშაო', 'საოჯახო', 'საცხოვრებელი')", name="check_type")
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
        CheckConstraint("direction IN ('შესვლა', 'გასვლა')", name="check_direction"),
    )

base.metadata.create_all(bind=engine)

