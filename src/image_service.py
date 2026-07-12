# coordinates the entire image-ingestion pipeline
import sqlite3
from image_database import ImageDatabase
import image_model
import image_processing
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class ImageService():
    def __init__(self,database:Path|ImageDatabase):
        
        if not type(database) == database.ImageDatabase:
            self.db = database.ImageDatabase(database)
            
        else:
            self.db = database
        
        logger.debug("Initialized ImageService...")



    