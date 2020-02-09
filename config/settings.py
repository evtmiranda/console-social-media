import os
from dotenv import load_dotenv

load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

CSV_FILE_PATH = os.environ.get("CSV_FILE_PATH")