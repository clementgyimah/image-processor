from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.image import image_exists
from app.services.analyze import analyze_image
from app.utils.auth import get_api_key

router = APIRouter()

class AnalyzeRequest(BaseModel):
    image_id: str

@router.post("/analyze")
def analyze(req: AnalyzeRequest, api_key: str = Depends(get_api_key)):
    if not image_exists(req.image_id):
        raise HTTPException(status_code=404, detail="Image not found")
    return analyze_image(req.image_id)
