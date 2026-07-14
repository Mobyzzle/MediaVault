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
# This is a heaping pile of garbafe, rework it
#    also make it a public function, let the processor to most of the heavy lifting
    def _build_asset_from_file(self,_title:str,_file_path:str|Path,_source_url:str|Path=None,_rating:int=1,_favourite:bool=False)-> Asset:

        logger.info("Starting to build an Asset..")


        image = self.processor._get_from_file(_file_path)
        self.processor.set_image(image)
        self.processor._verify_image()

        thumbnail = self.processor._create_thumbnail(Path("thumbnails"),file_name=Path(_file_path.stem))
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


# finish the ingestion pipeline, this also needs a lil rework
    def add_image(self,title:str,file_path:str|Path=None,source_url:str=None,rating:int=1,favourite:bool=False) -> Asset:
        path = Path(file_path)
        if not file_path and not source_url:
            raise ValueError("no file_path and no source_url defined")
        if path:

            processed_image = self.processor.process_image_from_file(file_path=file_path,title=title)
        else:
            raise ValueError("No Filepath given")

