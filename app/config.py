import os

UPLOAD_DIR = "uploads"
MAX_FILE_SIZE_MB = 5
ALLOWED_EXTENSIONS = ["jpeg", "jpg", "png"]

os.makedirs(UPLOAD_DIR, exist_ok=True)
