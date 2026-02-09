import datetime
import uuid
from sqlalchemy import Boolean, Boolean, Column, Integer, String, DateTime, ForeignKey, Uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


    
class User(Base):
    
    """
    The User model mirror of the database

    Returns:
        _type_: _description_
        
    Attributes:
            id (int): Primary key, auto-incremented user ID.
            username (str): Unique username for the user.
            email (str): Unique email address for the user.
            full_name (str): Full name of the user.
            
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, description="The user's username or phonenumber")
    email = Column(String, unique=True, index=True, nullable=True, description="The user's email address")
    # full_name = Column(String, nullable=True)
    role = Column(Integer, ForeignKey('roles.id'))  # 0: regular user, 1: admin
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False)
    u_uuid = Column(Uuid(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), onupdate=datetime.datetime.now(datetime.UTC), nullable=False)    

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"