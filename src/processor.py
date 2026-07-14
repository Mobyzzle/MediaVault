# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank
from asset import Asset
import logging
from PIL import Image
from pathlib import Path
import os
logger = logging.getLogger(__name__)

class Processor:
    
    def __init__(self):

        self.output_dir = Path("thumbnails")
        self._create_thumbnail_output()
        
        logger.info("Initialized Processor...")


    def _get_from_url(self,url):
        logger.debug("Not Implemented yet..")

    def _get_image_from_file(self,file_path:str|Path) -> Image.Image:
        
        path = Path(file_path)
        
        

        with Image.open(path) as im:
            logger.info("Image opened...")
            im.load()
            return im.copy()


    def process_image_from_file(self,file_path:str|Path,title:str) -> Asset: # make this the function that is actually called in vault.py
        logger.info("Starting to process image...")
        path = Path(file_path)
        
        self._verify_file(path)                     # File operations, move to its own function later on
        file_size  = self._get_file_size(path)      # <- this one returns BYTES, convert later
        img = self._get_image_from_file(path)       #   actually get a workable image
        
        thumbnail = self._create_thumbnail(img,title)          # change the title to hash later, so thumbnails are unique to each image, and to avoid duplicates    
        
        return Asset(
            title = title,
            file_path=file_path,
            file_size= file_size,
            thumbnail_path=thumbnail,
            width=img.width,
            height=img.height
        )

            
        

    def _file_operations(self,file_path:str|Path) -> None:
        pass

    def _create_thumbnail_output(self):
        if not self.output_dir.is_dir():
            self.output_dir.mkdir(exist_ok=True,parents=True)  
    

    def _create_thumbnail(self,image:Image.Image,title) -> Path: # there are some path issues here, fix them
        
        thumbnail = image.copy()
                
        thumbnail.thumbnail((150,150))

        output_dir = Path(self.output_dir)
        output_name = title

        output = Path(output_dir/f"{output_name}.webp")
        thumbnail.save(output,"webp",quality=80)
        logger.info("Thumbnail created...")
        return output
        


    def _verify_file(self,file_path:str|Path) -> None:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"Couldn't find file:{path}")


    def _get_file_size(self,file_path:str|Path) -> int:
        file_path = Path(file_path)
        
        size = os.stat(file_path).st_size
        
        return size
            
            






if __name__ == "__main__":
    processor = Processor()
    processor._get_file_size("thumbnails/bob.webp")
