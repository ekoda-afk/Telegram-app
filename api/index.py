from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

firebase_base64 = os.environ.get("FIREBASE_CREDENTIALS")
firebase_json = json.loads(base64.b64decode(firebase_base64).decode("utf-8"))
cred = credentials.Certificate(firebase_json)
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.get("/")
def root():
    return {"message": "Hello from Telegram Mini App!"}
