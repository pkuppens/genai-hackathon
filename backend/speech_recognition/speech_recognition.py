import whisper
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

class SpeechRecognitionRequest(BaseModel):
    model: Optional[str] = "turbo"

model_cache = {}

def get_model(model_name: str):
    if model_name not in model_cache:
        model_cache[model_name] = whisper.load_model(model_name)
    return model_cache[model_name]

@app.post("/recognize-speech")
async def recognize_speech(file: UploadFile = File(...), model: str = "turbo"):
    if file.content_type not in ["audio/wav", "audio/mpeg", "audio/mp3"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    audio_data = await file.read()
    model = get_model(model)

    result = model.transcribe(audio_data)
    transcript = result["text"]
    language = result["language"]

    return JSONResponse(content={"transcript": transcript, "language": language})
