from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    # create table users
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    username=Column(String,unique=True, nullable=False)
    email = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    posts = relationship("Post",back_populates="author")
    comments = relationship("Comment",back_populates="author")

class Post(Base):
    __tablename__="posts"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    content = Column(Text,nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"),nullable=False)

    author = relationship("User",back_populates="posts")
    comments = relationship("Comment",back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")


