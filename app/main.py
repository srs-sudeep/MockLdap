from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import AuthRequest, AuthResponse
from .mock_db import authenticate_user

app = FastAPI(title="Mock LDAP Service")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Mock LDAP Service",
        "version": "1.0.0",
        "status": "running"
    }

@app.post("/auth", response_model=AuthResponse)
async def authenticate(auth_request: AuthRequest):
    success, user_data, error = authenticate_user(
        auth_request.username,
        auth_request.password
    )
    
    if not success:
        return AuthResponse(
            success=False,
            error=error
        )
    
    return AuthResponse(
        success=True,
        user_data=user_data
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 