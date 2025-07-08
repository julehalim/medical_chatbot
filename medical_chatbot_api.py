from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fastapi.responses import FileResponse
import os
import logging

app = FastAPI()

# Configure logging to print to console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    user_message: str

# Initialize Azure AI Foundry client once
try:
    project = AIProjectClient(
        endpoint="https://jule-mcuf9sfz-swedencentral.cognitiveservices.azure.com",
        credential=DefaultAzureCredential(),
    )
    models = project.inference.get_azure_openai_client(api_version="2024-10-21")
    deployment_name = "medical-gpt4o"  # your deployment name
    logger.info("Azure AI client initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize Azure AI client: {e}")
    # Raise here or handle accordingly

SYSTEM_PROMPT = (
    "You are a helpful medical assistant. Provide accurate medical information but DO NOT diagnose "
    "or provide treatment advice. Always remind users to consult a healthcare professional."
)

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = models.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.user_message},
            ],
        )
        answer = response.choices[0].message.content
        logger.info(f"User message: {request.user_message}")
        logger.info(f"Bot response: {answer}")
        return {"answer": answer}
    except Exception as e:
        logger.error(f"Error during chat completion: {e}")
        raise HTTPException(status_code=500, detail="Failed to get response from Azure AI service.")

@app.get("/")
async def get_home():
    chat_html_path = os.path.join(os.getcwd(), "chat.html")
    if os.path.exists(chat_html_path):
        return FileResponse(chat_html_path)
    else:
        raise HTTPException(status_code=404, detail="chat.html not found.")
