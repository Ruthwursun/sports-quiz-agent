
import os

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load environment variables
load_dotenv()



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("hiii")
