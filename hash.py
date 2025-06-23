from passlib.context import CryptContext # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt(passsword: str):
    return pwd_context.hash(passsword)

def decrypt(password, hashed_pass):
    return pwd_context.verify(password, hashed_pass)