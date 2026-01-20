from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated

# ================
# User Schemas 
# ================

PasswordStr = Annotated[
    str,
    StringConstraints(min_length=6, max_length=72)
]

class UserCreate(BaseModel):
    email: EmailStr
    password: PasswordStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # ✅ Correct for Pydantic v2

# ================
# Auth Schemas
# ================

class Token(BaseModel):
    access_token: str
    token_type: str
