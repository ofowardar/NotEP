from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError,jwt
from fastapi import HTTPException,status

# Hash the password
pwd_context = CryptContext(schemes=["bcrypt"],deprecated ="auto")

#JWT sectet key
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password:str) -> str:
    """
    Hash The Password
    """
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str) -> bool:
    """
    Compare plain passwd and hashed passwd.
    """
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict , expires_delta:timedelta=None) -> str:
    """
    Create JWT TOKEN !
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict:
    """JWT token doğrula ve decode et"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token geçersiz"
            )
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token geçersiz veya süresi doldu"
        )