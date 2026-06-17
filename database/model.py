from pydantic import (
    BaseModel,
    EmailStr
)


# USER MODEL
class User(BaseModel):
    name: str
    email: EmailStr
    password: str


# LOGIN MODEL
class LoginUser(BaseModel):
    email: EmailStr
    password: str


# TEA MODEL
class Tea(BaseModel):
    tea_name: str
    price: float
    quantity: int
    category: str