from passlib.context import CryptContext
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Union

SECRET_KEY = "636e64956322901f1d573f739a64d0cb05b67d83ac150f8bc7fee89321496ca660c97ef3b5a1fac97f394f9c08038075a3bf6adc2b843e2d3a12e465b41d20259dd07a6a802bfa09c1e978384b0caeb081ca159c407eb5ccb5f358af3ff1e7126663901ca49cd5e95dff7e94534cef728d19c9797f0f0f6c3357ab17e8305b74ade1a418bd22105b30336db1a4fd29cbce0e8b60c160604dacf67bb04c46dc88e3058643725273e37dfd5434f39e8f00e15912f965f9f286fdff9cf3266497542abcfc00ffd79288c4c3e8008dfbbbc9ef9fd1044aae8d657c7048aff763afee2ba2396ff4b83ca1ea8a9eb46f72d25929f691e3991d9085a00f87bc585eb375"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_full_name(firstname: str, lastname: str) -> str:
     return f"{firstname} {lastname}"

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
