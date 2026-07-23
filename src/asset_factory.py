from .assets import ImageAsset, MediaAsset
from .enums import MediaType
import logging
from pathlib import Path
logger = logging.getLogger(__name__)
# responsibilieties: constructs the right Asset from given Data

class AssetFactory():




    def construct(self,media_type:MediaType,data:dict) -> MediaAsset:
        logger.info("Constructing Asset from Data")
        match media_type:
            case MediaType.IMAGE:
                return self._construct_image_asset(data)
            case MediaType.VIDEO:
                raise NotImplementedError(f"{media_type} is not yet implemented")
            case MediaType.UNKNOWN:
                  raise ValueError("Unknown File Type")

    def _construct_image_asset(self,data:dict) -> ImageAsset:
            logger.info("Trying to construct ImageAsset") 
            return ImageAsset(
            id= data.get("id", None),
            media_type = MediaType.IMAGE,
            title=data["title"],
            file_path=data["file_path"] if data["file_path"] is not None else None,
            source_url=data["source_url"] if data["source_url"] is not None else None,
            height=data["height"],
            width = data["width"],
            file_size = data["file_size"],
            thumbnail_path = Path(data["thumbnail_path"]) if data["thumbnail_path"] is not None else None,
            aspect_ratio = data["aspect_ratio"],
            file_hash = data["file_hash"],
            date_added = data.get("date_added", None),
            last_viewed= data.get("last_viewed", None),
            viewcount= data.get("viewcount", None),
            favourite=data.get("favourite",False),
            rating=data.get("rating",0)
            )


