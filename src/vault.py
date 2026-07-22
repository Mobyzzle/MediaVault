# coordinates the entire image-ingestion pipeline

from media_repository import Database
import logging
from pathlib import Path
from processors.image_processor import ImageProcessor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)
from media_downloader import Downloader
from media_type_detector import MediaTypeDetector,MediaType
from assets import MediaAsset,ImageAsset



class Vault:
    def __init__(self,database:Path|Database):
        
        self.IMAGE_OUTPUT = "images/"

        self.DEFAULT_THUMBNAIL_OUTPUT = "thumbnails/"

        # initialising all the components for Vault to drive, VROOM VROOM

        if not type(database) == Database:
            self.db = Database(database)
            
        else:
            self.db = database
        self.image_processor = ImageProcessor(self.DEFAULT_THUMBNAIL_OUTPUT)
        self.downloader = Downloader()
        self.detector = MediaTypeDetector()
        logger.info("Initialized Vault...")


    def get_by_id(self,id:int) -> MediaAsset:
        data = self.db.search_by_id(id)

        return MediaAsset.from_row(data)


# finish the ingestion pipeline, this also needs a lil rework
    def ingest_file(self,title:str,file_path:str|Path|None=None,source_url:str=None) -> ImageAsset:

        if file_path is None:             # Catch exception earlier instead of else block
            raise ValueError("No Filepath was given")
        
        validated_path = self._validate_path(file_path=file_path)
        
        
        try:
                processed_data = self.image_processor.process(validated_path,title,source_url)
                prototype_asset = ImageAsset.from_data(processed_data)
                stored_asset = self.db.insert_image(prototype_asset)
                return stored_asset
        except Exception:
            logger.debug("Image Ingestion failed")    # use this to see what goes wrong for now
            raise
        finally:
            logger.info("Finished processing image....")
                

  
        

    def ingest_from_url(self,title:str,source_url:str,save_to_file:bool=False) -> MediaAsset:

        if not source_url:
            raise ValueError("No Url was given")
        
        
        
        with self.downloader.download(source_url=source_url) as tempImage:
            logger.debug(tempImage.name)
            stored_asset = self.ingest_file(title,tempImage.name,source_url=source_url)
            if save_to_file:
                self.processor.save_image(tempImage.name,output_dir=self.IMAGE_OUTPUT,file_name=title) # <----- rework this entire block into a ingest_from_url function
            return stored_asset
            
        
    def _validate_path(self,file_path:str|Path) -> Path:
        return Path(file_path) 

