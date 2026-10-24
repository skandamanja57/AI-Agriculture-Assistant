import base64
import ollama

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot.ai_chatbot import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Agriculture Assistant API is running!"
    }


@app.post("/ask")
def ask_question(data: Question):
    answer = generate_answer(data.question)
    return {
        "question": data.question,
        "answer": answer
    }


@app.post("/detect-disease")
async def detect_disease(file: UploadFile = File(...)):
    """
    Accept a leaf image upload and use the local Llama3.2-vision model
    (or fall back to llama3.2 with a description prompt) to detect diseases.
    """
    image_bytes = await file.read()
    image_b64   = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """You are an expert plant pathologist and AI Agriculture Assistant.

Analyze the leaf image provided and:
1. Identify whether the leaf appears healthy or shows signs of disease / pest damage.
2. If diseased, name the most likely disease(s) (e.g., early blight, late blight, powdery mildew, bacterial spot, rust, leaf curl, etc.).
3. Describe the visible symptoms you observe (colour, spots, texture, lesions, yellowing, etc.).
4. Suggest practical management steps a farmer can take.
5. Recommend whether the farmer should consult a local agricultural extension officer.

Be concise, practical, and clear. If the image quality is too low to make a confident assessment, say so and advise re-uploading a clearer photo.
"""

    try:
        # Try vision-capable model first (llama3.2-vision if available)
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_b64]
                }
            ]
        )
        result = response["message"]["content"]
    except Exception:
        # Fallback: llama3.2 text model with a descriptive prompt
        try:
            fallback_prompt = (
                "You are an expert plant pathologist. A farmer has uploaded a leaf photo for disease analysis.\n"
                "Since image analysis is unavailable right now, provide general guidance:\n"
                "1. List the most common diseases for common crops (tomato, rice, wheat, potato).\n"
                "2. Describe their main visual symptoms.\n"
                "3. Suggest how to identify and manage each disease.\n"
                "4. Advise the farmer to consult an agricultural extension officer for a confirmed diagnosis."
            )
            response = ollama.chat(
                model="llama3.2",
                messages=[{"role": "user", "content": fallback_prompt}]
            )
            result = (
                "⚠️ Image analysis model (llama3.2-vision) is not available. "
                "Here is general plant disease guidance instead:\n\n"
                + response["message"]["content"]
            )
        except Exception as e:
            result = f"Error: Could not analyze the image. Please ensure Ollama is running. Details: {str(e)}"

    return {"result": result}
