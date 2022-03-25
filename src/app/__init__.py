from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
import logging

app = Flask(__name__)

meta = MetaData()
engine = create_engine("postgresql://ncr:ncr@localhost:5432/ncr")

logger = logging.getLogger('__name__')
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s:')
# file_handler = logging.FileHandler("logs/basic_log.log")
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

from src.app.controllers import *
