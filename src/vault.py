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

    def _build_asset_from_file(self,_title:str,_file_path:str|Path,_source_url:str|Path=None,_rating:int=1,_favourite:bool=False)-> Asset:
        image = self.processor._get_from_file(_file_path)
        self.processor.set_image(image)
        self.processor._verify_image()

        thumbnail = self.processor._create_thumbnail()
        file_size = self.processor._get_file_size(_file_path)


        if _favourite:
            favourite_placeholer = 1
        else:
            favourite_placeholer = 0


        return Asset(
            file_path=_file_path,
            source_url=_source_url,
            width = image.width,
            height = image.height,
            file_size = file_size,
            thumbnail= thumbnail,
            favourite=favourite_placeholer,
            title = _title,
            rating = _rating,

        )



    def add_image(self,title:str,file_path:str|Path=None,source_url:tuple[str,bool]=None,rating:int[range(1,10)]=1,favourite:bool=False) -> Asset:
        
        insertion_asset = self._build_asset_from_file(title,file_path,source_url,rating,favourite)
        return insertion_asset