# coordinates the entire image-ingestion pipeline

from database import Database
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class Vault():
    def __init__(self,database:Path|Database):
        
        if not type(database) == database.ImageDatabase:
            self.db = database.ImageDatabase(database)
            
        else:
            self.db = database
        
        logger.debug("Initialized ImageService...")



    