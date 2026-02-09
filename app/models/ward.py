from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import user


Base = declarative_base()

class Ward(Base):
    """
    The Ward model mirror of the database

    Returns:
        _type_: _description_
        
    Attributes:
            id (int): Primary key, auto-incremented ward ID.
            name (str): Name of the ward.
            location (str): Location of the ward.
            capacity (int): Capacity of the ward.
            
    """
    __tablename__ = 'wards'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    """Fullname of the ward 

    Returns:
        _type_: _description_
    """
    fullname = Column(String, unique=True, index=True, description="The ward's name")
    location = Column(String, nullable=True)
    capacity = Column(Integer)
    parent= Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Ward(id={self.id}, name={self.name}, location={self.location})>"