from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt(passsword: str) -> str:
    return pwd_context.hash(passsword)

def decrypt(password, hashed_pass) -> bool:
    return pwd_context.verify(password, hashed_pass)