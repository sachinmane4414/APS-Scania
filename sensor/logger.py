
import logging
import os
from datetime import datetime
import os

## Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
## Log Directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
## create folder if not availabe
os.makedirs(logs_path, exist_ok=True)
## Log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)