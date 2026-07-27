# coordinates the entire image-ingestion pipeline

from media_repository import MediaRepository
import logging
from pathlib import Path
from asset_factory import AssetFactory
from processors import Processor, ImageProcessor
from exceptions import AppError,not_yet_implemented
logger = logging.getLogger(__name__)
from media_downloader import Downloader
from media_type_detector import MediaTypeDetector,MediaType
from assets import MediaAsset



class Vault:
    def __init__(self):
        
        self.IMAGE_OUTPUT = "images/"
        self.DOWNLOAD_OUTPUT = "downloads/"
        self.DEFAULT_THUMBNAIL_OUTPUT = "thumbnails/"

        self.DEFAULT_DATABASE_PATH = "database/imagevault.db"
        # initialising all the components for Vault to drive, VROOM VROOM
        
        self.repository = MediaRepository(self.DEFAULT_DATABASE_PATH)
        self.processors = self._initialize_processors()
        self.asset_factory = AssetFactory()

        self.downloader = Downloader()
        self.detector = MediaTypeDetector()
        logger.info("Initialized Vault...")


    def get_by_id(self,id:int) -> MediaAsset:
        data = self.db.search_by_id(id)

        return MediaAsset.from_row(data)


# finish the ingestion pipeline, this also needs a lil rework
    def ingest_file(self,title:str,file_path:str|Path|None=None,source_url:str|None = None) -> MediaAsset:

        if file_path is None:             # Catch exception earlier instead of else block
            raise ValueError("No Filepath was given")
        
        path = self._validate_path(file_path=file_path) # this converts strings into Path objects, so no further conversion needed

        
        
        try:
                media_type = self.detector.detect(file_path=path)
                processor = self._get_processor(media_type=media_type)
                data = processor.process(file_path=path,title=title,source_url=source_url)         
                
                raw_asset = self.asset_factory.construct(media_type=media_type,data=data)
                stored_asset_data = self.repository.insert_asset(raw_asset)
                stored_asset = self.asset_factory.construct(data=stored_asset_data,media_type=MediaType(stored_asset_data["media_type"]))
                return stored_asset
        except Exception:
            logger.exception("Media insertion failed...")    # use this to see what goes wrong for now
            raise
        finally:
            logger.info("Media insertion attempt finished...")
                

  
        

    def ingest_from_url(self,title:str,source_url:str,save_to_file:bool=False) -> MediaAsset:

        if not source_url:
            raise ValueError("No Url was given")
        
        
        
        with self.downloader.download(source_url=source_url) as tempImage:
            logger.debug(tempImage.name)
            stored_asset = self.ingest_file(title,tempImage.name,source_url=source_url)
            if save_to_file:
                processor = self._get_processor(stored_asset.media_type)
                processor.save_image(tempImage.name,output_dir=self.DOWNLOAD_OUTPUT,file_name=title)
            return stored_asset
            
        
    def _validate_path(self,file_path:str|Path) -> Path:
        return Path(file_path) 

    def _initialize_processors(self) -> dict[Processor]:
        
        return {
            MediaType.IMAGE : ImageProcessor(self.DEFAULT_THUMBNAIL_OUTPUT)
        }

    def _get_processor(self,media_type:MediaType) -> Processor:
        if media_type is MediaType.UNKNOWN:
            raise ValueError("File type is not supported")
        if media_type not in self.processors:
            raise KeyError(f"no processor registered for {media_type}")
        return self.processors[media_type]

