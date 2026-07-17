import os
import streamlit as st
from dotenv import load_dotenv


# Load environment variables
load_dotenv()




GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
