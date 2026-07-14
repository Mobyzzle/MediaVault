# coordinates the entire image-ingestion pipeline

from database import Database
import logging
from pathlib import Path
from asset import Asset
from processor import Processor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)


class Vault:
    def __init__(self,database:Path|Database):
        



        if not type(database) == Database:
            self.db = Database(database)
            
        else:
            self.db = database
        self.processor = Processor()
        logger.debug("Initialized Vault...")
#
#

# finish the ingestion pipeline, this also needs a lil rework
    def add_image(self,title:str,file_path:str|Path=None,source_url:str=None,rating:int=1,favourite:bool=False) -> Asset:
        path = Path(file_path)
        if not file_path and not source_url:
            raise ValueError("no file_path and no source_url defined")
        if path:

            raw_asset = self.processor.process_image_from_file(file_path=file_path,title=title)
            return raw_asset
        else:
            raise ValueError("No Filepath given")

