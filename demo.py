from Hate.Logger import logging
logging.info("Welcome to our Data Science and Machine Learning Course!")
from Hate.Exception import CustomException
import sys
try:
    a=10/'b'
except Exception as e:
    raise CustomException(0,sys) from e