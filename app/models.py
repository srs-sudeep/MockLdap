from pydantic import BaseModel
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    FACULTY = "faculty"
    STUDENT = "student"

class LDAPUser(BaseModel):
    uid: str
    password: str
    cn: str  # Common Name (Full Name)
    mail: str
    employee_type: UserRole
    department: Optional[str] = None
    title: Optional[str] = None

class AuthRequest(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    success: bool
    user_data: Optional[dict] = None
    error: Optional[str] = None 