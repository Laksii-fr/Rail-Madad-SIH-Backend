from fastapi import UploadFile
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr, constr
from typing import *


class InitiatePasswordResetRequest(BaseModel):
    email: str


class ConfirmPasswordResetRequest(BaseModel):
    email: str
    confirmation_code: str
    new_password: constr(min_length=8)


class ConfirmUserRequest(BaseModel):
    email: str
    confirmation_code: str


class SignUpRequest(BaseModel):
    email: str
    password: constr(min_length=8)


class LoginRequest(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    User_name : str
    User_email : str
    OpenAPI_key : Optional[str] = None