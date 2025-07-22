from fastapi import FastAPI, UploadFile, File
from deepface import DeepFace
from typing import Dict
import shutil
import os
import uuid

app = FastAPI()

@app.post("/verify-face")
async def verify_face(img1: UploadFile = File(...), img2: UploadFile = File(...)) -> Dict:
    # Save uploaded files temporarily
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)
    
    img1_path = os.path.join(temp_dir, f"{uuid.uuid4()}.jpg")
    img2_path = os.path.join(temp_dir, f"{uuid.uuid4()}.jpg")

    with open(img1_path, "wb") as f1:
        shutil.copyfileobj(img1.file, f1)
    with open(img2_path, "wb") as f2:
        shutil.copyfileobj(img2.file, f2)

    try:
        result = DeepFace.verify(img1_path, img2_path, model_name="Facenet", enforce_detection=False)
        response = {
            "verified": result["verified"],
            "distance": result["distance"],
            "model": result["model"]
        }
    except Exception as e:
        response = { "error": str(e) }
    finally:
        os.remove(img1_path)
        os.remove(img2_path)

    return response
