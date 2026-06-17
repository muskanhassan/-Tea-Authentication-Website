from fastapi import (
    APIRouter,
    HTTPException,
    Response,
    Cookie
)

from configuration import users_collection
from database.model import User
from utils.hashing import (
    hash_password,
    verify_password
)

router = APIRouter()


# ==========================
# REGISTER USER
# ==========================
@router.post("/register")
async def register_user(user: User):

    # Check if user already exists
    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    # Hash password
    hashed_password = hash_password(
        user.password
    )

    # Convert user object to dictionary
    user_dict = dict(user)

    # Replace plain password with hashed password
    user_dict["password"] = (
        hashed_password
    )

    # Save to MongoDB
    users_collection.insert_one(
        user_dict
    )

    return {
        "message":
        "User registered successfully"
    }


# ==========================
# LOGIN USER
# ==========================
@router.post("/login")
async def login_user(
    user: User,
    response: Response
):

    # Find user in database
    db_user = users_collection.find_one(
        {"email": user.email}
    )

    # User not found
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verify password
    is_password_correct = (
        verify_password(
            user.password,
            db_user["password"]
        )
    )

    # Wrong password
    if not is_password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    # Set cookie after successful login
    response.set_cookie(
        key="user_email",
        value=user.email,
        httponly=True
    )

    return {
        "message":
        "Login successful"
    }


# ==========================
# PROFILE ROUTE
# ==========================
@router.get("/profile")
async def user_profile(
    user_email: str = Cookie(None)
):

    # Check login
    if not user_email:
        raise HTTPException(
            status_code=401,
            detail="Please login first"
        )

    return {
        "message":
        f"Welcome {user_email}"
    }


# ==========================
# LOGOUT USER
# ==========================
@router.post("/logout")
async def logout_user(
    response: Response
):

    # Delete cookie
    response.delete_cookie(
        key="user_email"
    )

    return {
        "message":
        "Logged out successfully"
    }