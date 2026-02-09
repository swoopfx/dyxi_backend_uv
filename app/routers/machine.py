from fastapi import APIRouter

router = APIRouter(prefix="/machine", tags=["Machine"])


@router.post("/visual-tracking")
async def visual_tracking():
    return {}

@router.post("/predict")
async def predict():
    return {}   

@router.post("/audio-tracking")
async def audio_tracking():
    return {}