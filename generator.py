from database import Citizens, ID_card, SessionLocal, Passport, Car_license, Car
from sqlalchemy.orm import Session
import datetime
import random
import string
from faker import Faker

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

@get_session
def creater(personal_id, first_name, last_name, birth_date, sex, address, db : Session):
    new_citizen = Citizens(personal_id = personal_id, first_name = first_name, last_name=last_name, 
                           birth_date=birth_date, sex=sex, address=address)
    db.add(new_citizen)

@get_session
def post_pass_id_carlicence(pers_id, card_id, pass_id, car_id, db: Session):
    new_id_card = ID_card(card_id=card_id, personal_id=pers_id, 
                     issue_date=datetime.date.today(), expiration_date=datetime.date.today() + datetime.timedelta(days=365))
    new_passport = Passport(passport_id=pass_id, personal_id=pers_id,
                     issue_date=datetime.date.today(), expiration_date=datetime.date.today() + datetime.timedelta(days=365))
    if car_id:
        new_car_license = Car_license(car_license_id=car_id, personal_id=pers_id,
                     issue_date=datetime.date.today(), expiration_date=datetime.date.today() + datetime.timedelta(days=365))
        post_car(pers_id=pers_id, cars_num=random.randint(0, 2))
        db.add(new_car_license)
    
    db.add(new_id_card)
    db.add(new_passport)
    

@get_session
def post_car(pers_id, cars_num, db: Session):
    cars = {"BMW": ["M5", "M4", "M3", "X6", "X5"], "Mercedes": ["C180", "Sprinter"], "Toyota": ["Prius", "4Runner", "Camry"], "Opel": ["Astra", "Vectra"]}
    
    for _ in range(cars_num):
        brand, model = random.choice(list(cars.items()))
        car_id = ''.join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(0, 999)).zfill(3) + ''.join(random.choices(string.ascii_uppercase, k=2))
        new_cars = Car(car_id=car_id, brand=brand, model=random.choice(model), owner=pers_id)
        
        db.add(new_cars)
    
fake = Faker("ka_GE")

for _ in range(25):
    sex = {"F": "მდ", "M": "მმ", "X": "-"}

    person = fake.profile(["name", "sex", "address"])
    person["first_name"], person["last_name"] = person["name"].split(' ')
    person["sex"] = sex[person["sex"]]
    person["birth_date"] = fake.date_between(start_date=datetime.date(1940, 1, 1), end_date="today")
    person["personal_id"] = str(random.randint(9999999999, 99999999999))
    person["passport_id"], person["card_id"] = [
        str(random.randint(10, 99)) + ''.join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(10000, 99999)) 
        for _ in range(2)]
    
    person["car_license_id"] = str(random.randint(10, 99)) + ''.join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(10000, 99999)) if random.randint(0, 1) else None

    creater(personal_id=person["personal_id"], first_name=person["first_name"], last_name=person["last_name"], 
            address=person["address"], sex=person["sex"], birth_date=person["birth_date"])
    
    post_pass_id_carlicence(pers_id=person["personal_id"], pass_id=person["passport_id"], card_id=person["card_id"], car_id=person["car_license_id"])