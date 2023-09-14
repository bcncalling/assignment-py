import os

from dotenv import load_dotenv

load_dotenv()


class config:
    MONGODB_URL = os.environ.get("MONGODB_URL")
    PORT = os.environ.get("PORT")
