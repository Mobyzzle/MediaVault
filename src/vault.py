# coordinates the entire image-ingestion pipeline

from database import Database
import logging
from pathlib import Path
from asset import Asset
from processor import Processor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)
from downloader import Downloader





class Vault:
    def __init__(self,database:Path|Database):
        
        self.IMAGE_OUTPUT = "images/"

        self.DEFAULT_THUMBNAIL_OUTPUT = "thumbnails/"

        # initialising all the components for Vault to drive, VROOM VROOM

        if not type(database) == Database:
            self.db = Database(database)
            
        else:
            self.db = database
        self.processor = Processor(self.DEFAULT_THUMBNAIL_OUTPUT)
        self.downloader = Downloader()

        logger.info("Initialized Vault...")



# finish the ingestion pipeline, this also needs a lil rework
    def ingest_file(self,title:str,file_path:str|Path|None=None,source_url:str=None) -> Asset:

        path = Path(file_path)
        
        if file_path != None:

            processed_asset = self.processor.process_image_from_file(file_path=path,title=title,source_url=source_url)
            stored_asset = self.db.insert_image(processed_asset)
            return stored_asset

        else:
            raise ValueError("No Filepath was given")
        

    def ingest_from_url(self,title:str,source_url:str,save_to_file:bool=False) -> Asset:

        if not source_url:
            raise ValueError("No Url was given")
        
        
        
        with self.downloader.download_image(source_url=source_url) as tempImage:
            logger.debug(tempImage.name)
            
            self.processor.verify_image(tempImage.name)
            stored_asset = self.ingest_file(title,tempImage.name,source_url=source_url)
            if save_to_file:
                self.processor.save_image(tempImage.name,output_dir=self.IMAGE_OUTPUT,file_name=title)
            return stored_asset
            
        
        

