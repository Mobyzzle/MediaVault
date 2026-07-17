# coordinates the entire image-ingestion pipeline

from database import Database
import logging
from pathlib import Path
from asset import Asset
from processor import Processor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)
from downloader import Downloader
from PIL import Image
class Vault:
    def __init__(self,database:Path|Database):
        

        DEFAULT_THUMBNAIL_OUTPUT = "thumbnails/"

        # initialising all the components for Vault to drive, VROOM VROOM

        if not type(database) == Database:
            self.db = Database(database)
            
        else:
            self.db = database
        self.processor = Processor(DEFAULT_THUMBNAIL_OUTPUT)
        self.downloader = Downloader()

        logger.info("Initialized Vault...")
#
#

# finish the ingestion pipeline, this also needs a lil rework
    def ingest_file(self,title:str,file_path:str|Path|None=None) -> Asset:

        path = Path(file_path)
        
        if file_path:

            raw_asset = self.processor.process_image_from_file(file_path=path,title=title)
            stored_asset = self.db.insert_image(raw_asset)
            return stored_asset

        else:
            raise ValueError("No Filepath was given")
        

    def ingest_from_url(self,title:str,source_url:str) -> Asset:

        if not source_url:
            raise ValueError("No Url was given")
        
        temp_file = self.downloader.create_temp_file(source_url)
        temp_file_path = Path(temp_file.name)
        logger.debug(temp_file.name)

        self.processor.verify_image(temp_file_path)
        with Image.open(temp_file.name) as im:
            im.show()
        temp_file.close()
        
        

