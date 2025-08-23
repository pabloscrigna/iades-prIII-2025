import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

mongo_url = os.getenv("MONGODB_URI")

# print(f"MongoDB URI: {mongo_url}")
