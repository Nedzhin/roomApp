from pydantic import BaseModel, field_validator 
from typing import Optional
from models.gender import Gender
from fastapi.exceptions import HTTPException
import re

class User(BaseModel):
    username: Optional[str]
    usersurname: Optional[str]
    gender: Optional[Gender]
    birthday: Optional[str]
    city: Optional[str]
    education: Optional[str]
    job: Optional[str]
    info: Optional[str]

    # @field_validator('username')
    # def validate_username(cls, v):
    #     if ' ' in v or not v:
    #         raise HTTPException(status_code=422)
    #     return v

    # @field_validator('email')
    # def validate_email(cls, v):
    #     if len(v) < 7 or not re.match(r"^.+@(\[?)[a-zA-Z0-9-.]+\.[a-zA-Z]{2,3}$", v):
    #         raise HTTPException(status_code=422)
    #     return v

    # @field_validator("age")
    # def validate_age(cls, v):
    #     if v < 0:
    #         raise HTTPException(status_code=422)
    #     return v

    # @field_validator("password")
    # def validate_password(cls, v):
    #     if " " in v or len(v) < 5:
    #         raise HTTPException(status_code=422)
    #     return v

    # @field_validator("birthday")
    # def validate_birthday(cls, v):
    #     if not re.match(r"^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$", v):
    #         raise HTTPException(status_code=422)
    #     return v

    # @validator("birthday")
    # def validate_birthday(cls, v):
    #     if not re.match("^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\\d\\d)$", v):
    #         raise HTTPException(status_code=422)
    #     return v