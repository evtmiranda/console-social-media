import os
from dotenv import load_dotenv

load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

APPLE_STORE_FILE_PATH = os.environ.get("APPLE_STORE_FILE_PATH")
FILE_PATH = os.environ.get("FILE_PATH")
TWITTER_TOKEN_URL = os.environ.get("TWITTER_TOKEN_URL")
TWITTER_SEARCH_URL = os.environ.get("TWITTER_SEARCH_URL")
TWITTER_KEY = os.environ.get("TWITTER_KEY")
TWITTER_SECRET_KEY = os.environ.get("TWITTER_SECRET_KEY")