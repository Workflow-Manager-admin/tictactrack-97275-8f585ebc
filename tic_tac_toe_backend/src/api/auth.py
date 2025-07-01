"""Authentication endpoints: user registration and login for the Tic Tac Toe backend."""
from fastapi import APIRouter
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


class UserRegister(BaseModel):
    username: str = Field(..., description="Username for registration")
    password: str = Field(..., description="Password for registration")


class UserLogin(BaseModel):
    username: str = Field(..., description="Username for login")
    password: str = Field(..., description="Password for login")


# PUBLIC_INTERFACE
@router.post(
    "/register",
    summary="Register a new user",
    description="Create a new user account.",
)
def register_user(user: UserRegister):
    """Endpoint to register a new user. Returns authentication token on success."""
    # Stub: Replace with actual registration logic
    return {
        "message": "User registered (stub)",
        "token": "fake-token",
    }


# PUBLIC_INTERFACE
@router.post(
    "/login",
    summary="Login an existing user",
    description="Authenticate a user and return an access token.",
)
def login_user(user: UserLogin):
    """Endpoint to login a user. Returns authentication token if credentials valid."""
    # Stub: Replace with actual auth logic
    return {
        "message": "Login successful (stub)",
        "token": "fake-token",
    }
