import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

print(f"DB: {DB_HOST}:{DB_PORT}, debug={DEBUG}")
