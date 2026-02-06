import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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
    email = Column(String, unique=True, index=True)
    # full_name = Column(String, nullable=True)
    role = Column(Integer, ForeignKey('roles.id'))  # 0: regular user, 1: admin
    hashed_password = Column(String)
    is_active = Column(Integer, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"