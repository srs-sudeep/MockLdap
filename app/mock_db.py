from .models import LDAPUser, UserRole
from passlib.hash import bcrypt

# Mock LDAP database
mock_users = {
    # Faculty members
    "john.doe": LDAPUser(
        uid="john.doe",
        password=bcrypt.hash("faculty123"),
        cn="John Doe",
        mail="john.doe@university.edu",
        employee_type=UserRole.FACULTY,
        department="Computer Science",
        title="Professor"
    ),
    "jane.smith": LDAPUser(
        uid="jane.smith",
        password=bcrypt.hash("faculty456"),
        cn="Jane Smith",
        mail="jane.smith@university.edu",
        employee_type=UserRole.FACULTY,
        department="Mathematics",
        title="Associate Professor"
    ),
    
    # Students
    "alice.student": LDAPUser(
        uid="alice.student",
        password=bcrypt.hash("student123"),
        cn="Alice Johnson",
        mail="alice.j@university.edu",
        employee_type=UserRole.STUDENT,
        department="Computer Science"
    ),
    "bob.student": LDAPUser(
        uid="bob.student",
        password=bcrypt.hash("student456"),
        cn="Bob Wilson",
        mail="bob.w@university.edu",
        employee_type=UserRole.STUDENT,
        department="Mathematics"
    ),
}

def get_user(username: str) -> LDAPUser:
    return mock_users.get(username)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str) -> tuple[bool, dict | None, str | None]:
    user = get_user(username)
    
    if not user:
        return False, None, "User not found"
        
    if not verify_password(password, user.password):
        return False, None, "Invalid password"
        
    # Return user data without password
    user_dict = user.dict(exclude={'password'})
    return True, user_dict, None 