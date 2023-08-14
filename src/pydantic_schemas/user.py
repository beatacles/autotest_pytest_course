from pydantic import BaseModel, field_validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int = 0
    name: str
    email: str
    gender: Genders
    status: Statuses

    @field_validator('email')
    def check_email(cls, email):
        if "@" in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)