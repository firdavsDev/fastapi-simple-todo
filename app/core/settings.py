import os

from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()


class Settings:
    PROJECT_NAME: str = "FastAPI To-Do App"
    PROJECT_EMAIL: str = "DavronbekDev"
    DESCRIPTION: str = "A simple To-Do app built with FastAPI"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "1.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL")


settings = Settings()
