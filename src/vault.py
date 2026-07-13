# coordinates the entire image-ingestion pipeline

from database import Database
import logging
from pathlib import Path
from processor import Processor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)


class Vault:
    def __init__(self,database:Path|Database):
        
        if not type(database) == Database:
            self.db = Database(database)
            
        else:
            self.db = database
        
        logger.debug("Initialized Vault...")


    def add_image(self,title:str=None,file_path:str|Path = None,source_url:str=None):
        
        not_yet_implemented()