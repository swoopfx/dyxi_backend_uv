from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Roles(Base):
    """
    The Role model mirror of the database

    Returns:
        _type_: _description_
        
    Attributes:
            id (int): Primary key, auto-incremented role ID.
            name (str): Name of the role.
            description (str): Description of the role.
            
    """
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, description="The role's name")
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name}, description={self.description})>"