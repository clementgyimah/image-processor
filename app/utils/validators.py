from fastapi import UploadFile, HTTPException
from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB

def validate_file(file: UploadFile):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")
    file.file.seek(0, 2)  # Move cursor to end
    size = file.file.tell() / (1024 * 1024)  # MB
    file.file.seek(0)
    if size > MAX_FILE_SIZE_MB:
        raise HTTPException(status_code=400, detail="File too large")
