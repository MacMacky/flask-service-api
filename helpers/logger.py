import logging
import datetime
from os import makedirs
from config import LOGS_PATH

class Log:
    date = str(datetime.date.today())
    INFO = logging.INFO
    ERR = logging.ERROR
    
    @staticmethod
    def logFilename() -> str:
        return f"{LOGS_PATH}MLShopAdminLogs{Log.date}.log"
    
    @staticmethod
    def date_format() -> str:
        return "%Y-%m-%d %H:%M:%S"
    
    @staticmethod
    def format() -> str:
        return '[%(asctime)s.%(msecs)03d %(levelname)s %(funcName)s - %(message)s]'



def make_logs_dir():
   try:
     makedirs(LOGS_PATH,exist_ok=True)
   except BaseException as e:
     print(e.msg)

make_logs_dir()

logging.basicConfig(
  filename=Log.logFilename(),
  datefmt=Log.date_format(),
  level=Log.INFO,
  format=Log.format(),
)
