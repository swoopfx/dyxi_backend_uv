from fastapi import APIRouter

router = APIRouter(prefix="/machine", tags=["Machine"])


@router.post("/visual-tracking")
async def visual_tracking():
    return {}