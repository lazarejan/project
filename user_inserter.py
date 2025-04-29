from database import get_session, Citizens
from sqlalchemy.orm import Session
import datetime
import random
from faker import Faker

@get_session
def creater(personal_id, first_name, last_name, birth_date, sex, address, db : Session):
    new_citizen = Citizens(personal_id = personal_id, first_name = first_name, last_name=last_name, 
                           birth_date=birth_date, sex=sex, address=address)
    db.add(new_citizen)

fake = Faker("ka_GE")

for _ in range(5):
    sex = {"F": "მდ", "M": "მმ", "X": "-"}

    person = fake.profile(["name", "sex", "address"])
    person["first_name"], person["last_name"] = person["name"].split(' ')
    person["sex"] = sex[person["sex"]]
    person["birth_date"] = fake.date_between(start_date=datetime.date(1940, 1, 1), end_date="today")
    person["personal_id"] = str(random.randint(9999999999, 99999999999))

    creater(personal_id=person["personal_id"], first_name=person["first_name"], last_name=person["last_name"], 
            address=person["address"], sex=person["sex"], birth_date=person["birth_date"])
