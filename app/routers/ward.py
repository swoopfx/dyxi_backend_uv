from fastapi import APIRouter
from app.schemas.request.registerSchema import RegisterSchema
from starlette.responses import JSONResponse
from starlette import status

router = APIRouter(prefix="/ward", tags=["Ward"])

@router.post("/create-ward", status_code=status.HTTP_201_CREATED)
async def create_ward(ward_request: RegisterSchema):
    pass

@router.get("/get-ward/{ward_uuid}")
async def get_ward(ward_uuid: str):
    pass

@router.get("/get-wards")
async def get_wards():
    pass

@router.put("/update-ward")
async def update_ward(ward_uuid: str, ward_request: RegisterSchema):
    pass

@router.post("/activate-ward")
async def activate_ward(ward_uuid: str):
    pass    

@router.post("/deactivate-ward")
async def deactivate_ward(ward_uuid: str):
    pass