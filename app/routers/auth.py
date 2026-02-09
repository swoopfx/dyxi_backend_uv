from fastapi import APIRouter
from app.schemas.request.registerSchema import RegisterSchema
from starlette.responses import JSONResponse
from starlette import status

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login():
    return {"message": "Login endpoint"}    


@router.post("/register",status_code=status.HTTP_201_CREATED)
async def register(register_request: RegisterSchema):
    pass
          
      

@router.post("/logout")
async def logout():
    return {"message": "Logout endpoint"}   

@router.post("/refresh")
async def refresh():
    return {"message": "Refresh token endpoint"}

@router.post("/reset-password")
async def reset_password():
    return {"message": "Reset password endpoint"}   

