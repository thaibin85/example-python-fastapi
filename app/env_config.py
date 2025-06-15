import os
from dotenv import load_dotenv
load_dotenv()
# Load environment variables from .env file
# If you want to use a different file, you can specify the path like this:
# load_dotenv(dotenv_path='path/to/your/.env')
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")