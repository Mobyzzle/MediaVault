# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank
from asset import Asset
import logging
from PIL import Image
from pathlib import Path
import os
logger = logging.getLogger(__name__)

class Processor:
    
    def __init__(self):
        self.image = Image.Image
        self.image_file_size = int
        logger.info("Initialized Processor...")

    def set_image(self,source:Image.Image) -> None:
        logger.info("Image loaded into Processor....")
        self.image = source
        
    def clear_processor(self) -> None:
        logger.info("Processor cache cleared")
        self.image = None

    def _create_thumbnail(self,output_dir:str|Path,file_name:str) -> Path:
        try:
            img = self.image.copy()
                
            img.thumbnail((150,150))
            output = f"{Path(output_dir)}/{file_name}.webp"
            img.save(output)
            logger.info("Thumbnail created...")
            return Path(output)
        except Exception as _e:
            logger.debug(_e)


    def _verify_image(self) -> None:
        img = self.image.copy()
        img.verify()
        logger.info("Image verified...")

    
        

    def _get_from_url(self,):
        logger.debug("Not Implemented yet..")

    def _get_from_file(self,file_path:str|Path,set:bool=False) -> Image.Image:
        source = Path(file_path)

        try:

            with Image.open(source) as im:
                logger.info("Image opened as ImageFile")
                
                if set:
                    self.set_image(im)
                    return None
                return im
        except Exception as e:
            logger.debug(e)

    def _get_file_size(self,source:str|Path) -> int:
        return os.stat(source).st_size
            
            






if __name__ == "__main__":
    print("fuck you")