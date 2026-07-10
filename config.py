import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Modèle Groq (ex: llama-3.3-70b-versatile ou le modèle spécifique demandé)
MODEL_NAME = "llama-3.3-70b-versatile"  
TEMPERATURE = 0.0

if not GROQ_API_KEY:
    raise ValueError("La variable GROQ_API_KEY n'est pas configurée dans le fichier .env")