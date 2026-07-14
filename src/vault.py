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
        logger.info("Initialized Vault...")
#
#

# finish the ingestion pipeline, this also needs a lil rework
    def add_image(self,title:str,file_path:str|Path|None=None,source_url:str|None=None) -> Asset:

        if not file_path and not source_url:
            raise ValueError("no file_path and no source_url defined")
        if file_path:

            raw_asset = self.processor.process_image_from_file(file_path=file_path,title=title)
            stored_asset = self.db.insert_image(raw_asset)
            return stored_asset
        elif source_url and not file_path:
            not_yet_implemented()
        else:
            raise ValueError("No Filepath given")

