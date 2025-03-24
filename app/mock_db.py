from .models import LDAPUser, UserRole
from passlib.hash import bcrypt

# Mock LDAP database
mock_users = {
    # Professors
    "amitdhar": LDAPUser(
        ldapid="amitdhar",
        password=bcrypt.hash("faculty123"),
        cn="Amit Kumar Dhar",
        email="amitdhar@iitbhilai.ac.in",
        role=UserRole.INSTRUCTOR,
        department="Computer Science",
        insti_id="20230001"
    ),
    "dhruvpratapsingh": LDAPUser(
        ldapid="dhruvpratapsingh",
        password=bcrypt.hash("faculty456"),
        cn="Dhruv Pratap Singh",
        email="dhruvpratapsingh@iitbhilai.ac.in",
        role=UserRole.INSTRUCTOR,
        department="Mathematics",
        insti_id="20230002"
    ),
    
    # Students
    "sudeepranjan": LDAPUser(
        ldapid="sudeepranjan",
        password=bcrypt.hash("student123"),
        cn="Sudeep Ranjan Sahoo",
        email="sudeepranjan@iitbhilai.ac.in",
        role=UserRole.STUDENT,
        department="Computer Science",
        insti_id="12141600"
    ),
    "lalaram": LDAPUser(
        ldapid="lalaram",
        password=bcrypt.hash("student456"),
        cn="Lala Ram",
        email="lalaram@iitbhilai.ac.in",
        role=UserRole.STUDENT,
        department="Mathematics",
        insti_id="12311370"
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