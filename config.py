from dotenv import load_dotenv
from pathlib import Path
from os import getenv

env_path = Path(".env")

load_dotenv(dotenv_path=env_path)


DBHOST = getenv("DBHOST")
DBPORT = getenv("DBPORT")
DBUSER = getenv("DBUSER")
DBPASS = getenv("DBPASSWORD")
LOGS_PATH = getenv("LOGS_PATH_DEV") if getenv("ENV") == "development"  else getenv("LOGS_PATH_PROD")
