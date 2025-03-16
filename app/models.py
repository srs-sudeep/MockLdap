from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    INSTRUCTOR = "instructor"
    STUDENT = "student"

class LDAPUser(BaseModel):
    ldapid: str
    password: str
    cn: str  # Common Name (Full Name)
    email: str
    role: UserRole
    department: str
    insti_id: str = Field(..., min_length=8, max_length=8)  # 8 digit number

class AuthRequest(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    success: bool
    user_data: Optional[dict] = None
    error: Optional[str] = None 