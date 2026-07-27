from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

MODEL_NAME = "llama-3.3-70b-versatile"

TEMPERATURE = 0

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)