import os
import shutil
from uuid import uuid4
from fastapi import UploadFile
from app.config import UPLOAD_DIR
from app.utils.logger import logger

def save_image(file: UploadFile) -> str:
    image_id = str(uuid4())
    extension = file.filename.split(".")[-1]
    file_path = os.path.join(UPLOAD_DIR, f"{image_id}.{extension}")

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    logger.info(f"Saved image with ID {image_id} as {file_path}")
    return image_id


def image_exists(image_id: str) -> bool:
    files = os.listdir(UPLOAD_DIR)
    logger.info(f"Checking {image_id} against files: {files}")
    for f in files:
        if f.split(".")[0] == image_id:  # match exact ID, ignoring extension
            logger.info(f"Image {image_id} exists as {f}")
            return True
    logger.info(f"Image {image_id} does not exist")
    return False
