
from pydantic import BaseModel, Field


class RegisterSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(... )
    #regex=r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$')
    password: str = Field(..., min_length=8)
    role: int = Field(..., ge=0, le=1)  # 0: regular user, 1: admin 