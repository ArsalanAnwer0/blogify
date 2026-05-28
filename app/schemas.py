from pydantic import BaseModel, EmailStr 
from datetime import datetime

# User Schemas

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str 

class UserResponse(BaseModel):
    id: int
    username: str 
    email: str 
    created_at: datetime

    model_config = {"from_attributes": True}

# Post Schemas

class PostCreate(BaseModel):
    title: str
    content: str 
    published: bool = True 

class PostResponse(BaseModel):
    id: int 
    title: str 
    content: str 
    published: bool 
    created_at: datetime 
    author_id: int 

    model_config = {"from_attributes": True}

# Comment Schemas

class CommentCreate(BaseModel):
    content: str 

class CommentResponse(BaseModel):
    id: int 
    content: str 
    created_at: datetime 
    author_id: int 
    post_id: int 

    model_config = {"from_attributes": True}


