from fastapi import HTTPException, Security, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from passlib.context import CryptContext
import secrets
from typing import Optional, Dict
from storage import load_students

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Security schemes
basic_security = HTTPBasic(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)

# In-memory token store
TOKENS: Dict[str, str] = {}

def authenticate_basic(creds: HTTPBasicCredentials) -> Optional[str]:
    if not creds: return None
    students = load_students()
    user = students.get(creds.username)
    if not user or not verify_password(creds.password, user["password_hash"]):
        return None
    return creds.username

def authenticate_bearer(token: Optional[str]) -> Optional[str]:
    return TOKENS.get(token) if token else None

async def get_current_username(
    request: Request,
    basic_creds: Optional[HTTPBasicCredentials] = Security(basic_security),
    token: Optional[str] = Security(oauth2_scheme),
) -> str:
    auth_header = request.headers.get("authorization", "")
    username = authenticate_basic(basic_creds) if auth_header.lower().startswith("basic") else authenticate_bearer(token)

    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated.",
            headers={"WWW-Authenticate": 'Basic realm="grades", Bearer'}
        )
    return username
