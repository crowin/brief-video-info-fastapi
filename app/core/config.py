import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "your-telegram-token")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")