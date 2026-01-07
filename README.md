# Image Analysis API (FastAPI)

A simple backend service that allows a mobile app to:

1. Upload an image (JPEG or PNG, max 5MB)
2. Perform mock “AI-style” analysis on the image
3. Return structured JSON results

This project demonstrates backend API design, file handling, basic validation, authentication, and end-to-end thinking from mobile → backend → response.

---

REQUIREMENTS

For local (non-Docker) run:

- Python 3.11+
- pip
- Virtual environment support

For Docker run:

- Docker Desktop installed and running

---

PROJECT STRUCTURE

```
app/
├── main.py
├── routes/
│ ├── upload.py
│ └── analyze.py
├── services/
│ ├── image_service.py
│ └── analysis_service.py
├── utils/
│ ├── validators.py
│ ├── auth.py
│ └── logger.py
├── config.py
uploads/ (runtime-generated, ignored in git)
Dockerfile
requirements.txt
README.md
```

---

RUNNING THE PROJECT (OPTION 1: LOCAL PYTHON)

1. Clone the repository and navigate into it

Using SSH:

`git clone git@github.com:clementgyimah/image-processor.git`

Using HTTPS:

`git clone https://github.com/clementgyimah/image-processor.git`

Then:

`cd image-processor`

2. Create and activate virtual environment

`python -m venv venv`

`source venv/bin/activate` (macOS / Linux)

`venv\Scripts\activate` (Windows)

3. Install dependencies

`pip install -r requirements.txt`

4. Create uploads directory (required)

`mkdir uploads`

5. Run the FastAPI server

`uvicorn app.main:app --reload`

6. Open Swagger UI

http://127.0.0.1:8000/docs

---

RUNNING THE PROJECT (OPTION 2: DOCKER)

1. Build Docker image

`docker build -t image-processor .`

2. Run Docker container

`docker run -p 8000:8000 image-processor`

NOTE:

- The uploads/ directory is created automatically inside the Docker container at runtime.
- No manual folder creation is required when running with Docker.

3. Open Swagger UI

http://127.0.0.1:8000/docs

---

API AUTHENTICATION

All endpoints require an API key.

Header:
`api-key: veefyedprocessor2026`

---

API ENDPOINTS

POST /upload

Uploads an image.

- Content-Type: multipart/form-data
- Supported formats: JPEG, PNG
- Max file size: 5MB

Response:

```
{
  "image_id": "abc123"
}
```

---

POST /analyze

Performs mock analysis on an uploaded image.

Request body:

```
{
"image_id": "abc123"
}
```

Response:

```
{
  "image_id": "abc123",
  "skin_type": "Oily",
  "issues": ["Hyperpigmentation"],
  "confidence": 0.87
}
```

Errors:

- 404 if image_id does not exist
- 400 for invalid input

---

LOGGING

Basic logging is enabled to track:

- Image uploads
- Image existence checks
- Analysis requests

Logs are printed to stdout.

---

GITIGNORE

Recommended .gitignore contents:

venv/
**pycache**/
\*.pyc
uploads/

IMPORTANT FOR NEW USERS:

- The uploads/ directory is intentionally ignored
- After cloning the repository, you MUST recreate it manually:

mkdir uploads

This directory is used to store uploaded images at runtime.

---

NOTES AND ASSUMPTIONS

- Image analysis logic is mocked (no real AI/ML)
- Images are stored locally on disk
- API key is hardcoded for simplicity
- No database is used
- Designed for clarity and correctness over production hardening

---

WHAT I WOULD IMPROVE FOR PRODUCTION

- Persistent storage (S3 or database)
- Real authentication (OAuth / JWT)
- Background processing for analysis
- Rate limiting
- Structured logging
- CI/CD pipeline

---
