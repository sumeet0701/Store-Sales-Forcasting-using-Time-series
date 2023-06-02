import logging
import os
import sys
from datatime import datetime

# creating logs directory to store log in files
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# creating Log_dir if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

#Creating file path for projects.
log_file_path = os.path.join(LOG_DIR, file_name)


logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)