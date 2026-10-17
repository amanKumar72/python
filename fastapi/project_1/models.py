from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

class UsersResponse(BaseModel):
    users: list[User]
    status: str
    success: bool