"""
    Handles password hashing and verification

"""

from passlib.context import CryptContext

""" Password hashing configuartion"""
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    """ Hash plain password """
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str) -> bool:
    """ Verif plain password against hashed password """
    return pwd_context.verify(plain_password,hashed_password)
