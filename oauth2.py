from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import status,HTTPException
import jwttoken
outh2_scheme=OAuth2PasswordBearer(tokenUrl='login')
def get_current_user(token: str= Depends(outh2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return jwttoken.verify_token(token,credentials_exception)