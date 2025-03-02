from .models import LDAPUser, UserRole
from passlib.hash import bcrypt

# Mock LDAP database
mock_users = {
    # Professors
    "john.doe": LDAPUser(
        ldapid="john.doe",
        password=bcrypt.hash("faculty123"),
        cn="John Doe",
        email="john.doe@university.edu",
        role=UserRole.PROFESSOR,
        department="Computer Science",
        insti_id="20230001"
    ),
    "jane.smith": LDAPUser(
        ldapid="jane.smith",
        password=bcrypt.hash("faculty456"),
        cn="Jane Smith",
        email="jane.smith@university.edu",
        role=UserRole.PROFESSOR,
        department="Mathematics",
        insti_id="20230002"
    ),
    
    # Students
    "alice.student": LDAPUser(
        ldapid="alice.student",
        password=bcrypt.hash("student123"),
        cn="Alice Johnson",
        email="alice.j@university.edu",
        role=UserRole.STUDENT,
        department="Computer Science",
        insti_id="20230003"
    ),
    "bob.student": LDAPUser(
        ldapid="bob.student",
        password=bcrypt.hash("student456"),
        cn="Bob Wilson",
        email="bob.w@university.edu",
        role=UserRole.STUDENT,
        department="Mathematics",
        insti_id="20230004"
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