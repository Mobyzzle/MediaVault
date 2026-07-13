# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank
from asset import Asset
import logging
from PIL import Image, ImageFile
from pathlib import Path
import os
logger = logging.getLogger(__name__)

class Processor:
    

    

    def _create_thumbnail(source:str|Path,output_dir:str|Path,file_name:str) -> Path:
        try:
            with Image.open(source) as im:
                
                im.thumbnail((150,150))
                im.save(f"{Path(output_dir)}/{file_name}.webp")
        except Exception as _e:
            logger.debug(_e)
    def _verify_image(source:str|Path) -> None:

        with Image.open(source) as im:
            im.verify()



    def _get_from_url():
        logger.debug("Not Implemented yet..")

    def _get_from_file(file_path:str|Path) -> dict:
        source = Path(file_path)

        try:
            with Image.open(source) as im:
                return im
        except Exception as e:
            logger.debug(e)
            
            
            






if __name__ == "__main__":
    print("fuck you")