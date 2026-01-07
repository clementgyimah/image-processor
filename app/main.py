from fastapi import FastAPI
from app.routes import upload, analyze

app = FastAPI(title="Image Processor")

app.include_router(upload.router)
app.include_router(analyze.router)

@app.get("/")
def root():
    return {"message": "Hey, welcome to the image processor API!"}
