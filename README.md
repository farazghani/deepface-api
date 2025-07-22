# 👥 DeepFace Face Verification API

A lightweight FastAPI-based REST API that verifies whether two face images belong to the same person using the [DeepFace](https://github.com/serengil/deepface) library.

---

## ⚙️ Installation

1. **Clone the repository**

git clone https://github.com/farazghani/deepface-api.git
cd deepface-api


## Install dependencies


pip install -r requirements.txt

## 🚀 Run the Server
uvicorn app:app --reload

## Face Verification Endpoint
POST /verify-face
