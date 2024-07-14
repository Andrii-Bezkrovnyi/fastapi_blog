from pydantic import BaseModel
from pydantic.config import ConfigDict

class UserBase(BaseModel):
    email: str

    class Config:
        arbitrary_types_allowed = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        arbitrary_types_allowed = True

class PostBase(BaseModel):
    text: str

    class Config:
        arbitrary_types_allowed = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        arbitrary_types_allowed = True
