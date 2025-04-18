from database import get_session, Citizens
from sqlalchemy.orm import Session

@get_session
def creater(p, n, l, d, s, a, ss : Session = None):

    new_citizen = Citizens(
        personal_id = p, name = n, last_name=l, birth_date=d, sex=s, address=a
    )
    
    ss.add(new_citizen)
    print("Added:", new_citizen, ss)

creater("12345678910", "Lazare", "Janili", "2000-11-24", "male", "Tbilisi")