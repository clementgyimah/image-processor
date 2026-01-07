from fastapi import APIRouter, UploadFile, File, Depends
from app.utils.validators import validate_file
from app.services.image import save_image
from app.utils.auth import get_api_key

router = APIRouter()

@router.post("/upload")
def upload_image(file: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    validate_file(file)
    image_id = save_image(file)
    return {"image_id": image_id}