from pydantic import BaseModel, Field, field_validator
from models.gender import Gender
from fastapi.exceptions import HTTPException
import re

class User(BaseModel):
    username: str #= Field(example="tawfiq")
    usersurname: str #= Field(example="nurseiit@gmail.com")
    gender: Gender #= Field(example="male")
    birthday: str #= Field(example="19/05/2006")
    city: str
    education: str
    job: str
    info: str
    #password: str #= Field(examples="nskmasdmsakm")
    #age: int #= Field(examples=21)
    
    
    # city: str = Field(example="Moscow")
    # education: str = Field(example="Study")
    # job: str = Field(example="IT")
    # info: str = Field(example="I love solving maths problems")

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "username" : "Nurseiit",
    #             "email" : "nurseiit@gmail.com",
    #             "password" : "12132",
    #             "age" : 12,
    #             "gender" : "male",
    #             "birthday" : "19/02/2002"
    #         }
    #     }

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