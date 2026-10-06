from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ["DB_HOST"])
print(os.environ["DB_PORT"])
print(os.environ["DEBUG"])
