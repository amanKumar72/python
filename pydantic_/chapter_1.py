from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator, computed_field
from typing import List, Dict, Optional
import re
from datetime import datetime

# pydantic with python typing
# it validate types of variables and make sure that types are correct
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    skills: List[str]
    dob: datetime
    metadata: Optional[Dict[str, str]] = None
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda dt: dt.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


# user_data = { 'id': 1, 'name': 'John Doe', 'email': '@', 'is_active': True} # correct
user_data = { 'id': "121", 'name': 'John Doe', 'email': '@', 'is_active': True, 'skills': ["python", "121", "c++"], 'dob': '1999-12-12 12:12:12'} # correct default conversion is possible for int from string
# user_data = { 'id': '123a', 'name': 'John Doe', 'email': '@', 'is_active': True} # will give error cause 'a' is not a valid int
user = User(**user_data) # unpack the dict and create user object
print(user)
print(user.model_dump_json(indent=2))
print(user.model_dump())

# Employee Schema with Field
'''

Field(
    ..., # means required
    description="Employee ID", # description of the field
    example="12345", # example of the field
    min_length=5, # minimum length of the field
    max_length=10, # maximum length of the field
    gt=0, # greater than 0
    ge=0, # greater than or equal to 0
    lt=100, # less than 100
    le=100, # less than or equal to 100
    regex=r"^[a-zA-Z0-9]+$", # regex pattern
)
'''
class Employee(BaseModel):
    employee_id: str = Field(..., description="Employee ID", example="12345")
    name: str = Field(..., description="Employee Name", example="John Doe", min_length=2, max_length=100)
    email: str = Field(..., description="Employee Email", example="[EMAIL_ADDRESS]")
    role: str = Field(..., description="Employee Role", example="Software Engineer")
    salary: float = Field(..., description="Employee Salary", example=100000.00, ge=0, le=1000000)
    mobile: str = Field(..., description="Employee Mobile", example="1234567890", pattern=r'^[6-9][0-9]{9}$')
    is_active: bool = Field(..., description="Employee Status", example=True)
    skills: List[str] = Field(..., description="Employee Skills", example=["python", "java", "c++"])
    metadata: Optional[Dict[str, str]] = Field(None, description="Employee Metadata", example={"project": "project1", "department": "engineering"})



# field_validator=> field_validator is used to validate a single field
# model_validator=> model_validator is used to validate the entire model

class UserSignUP(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str
    
    @field_validator("email")
    def email_validator(cls, value):
        if "@" not in value:
            raise ValueError("Email is not valid")
        return value
    
    @field_validator("password", "confirm_password")
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

    @model_validator(mode='after')
    def match_confirm_password(cls, value):
        if value.password != value.confirm_password:
            raise ValueError("Passwords do not match")
        return value

# computed_field => 
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

    @computed_field
    @property
    def full_address(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip}"


