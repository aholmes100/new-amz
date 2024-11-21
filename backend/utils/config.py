from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("AMZ_CLIENT_ID")
CLIENT_SECRET = os.getenv("AMZ_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("AMZ_REFRESH_TOKEN")
PROFILE_ID = os.getenv("AMZ_PROFILE_ID")