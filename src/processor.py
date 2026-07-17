# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank
from asset import Asset
import logging
from PIL import Image
from pathlib import Path
import os
import uuid
logger = logging.getLogger(__name__)

class Processor:
    
    def __init__(self,thumbnail_output:str|Path):

        self.thumbnail_output_dir = Path(thumbnail_output)
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


    def process_image_from_file(self,file_path:str|Path,title:str) -> Asset: # <-- THIS FOOKIN WORKS HELL FKN YEAH!! good job me c:
        logger.info("Starting to process image...")
        
        
            
        
        self.verify_image(file_path)                    # <--- this one checks if it is a file and already throws an exception, no further checking needed
        file_size  = self._get_file_size(file_path)      # 
        img = self._get_image_from_file(file_path)       #  
        
        thumbnail = self._create_thumbnail(img,title)          # change the title to hash later, so thumbnails are unique to each image, and to avoid duplicates    
        
        return Asset(
            title = str(title),
            file_path=str(file_path),
            file_size= int(file_size),
            thumbnail_path=str(thumbnail),
            width=int(img.width),
            height=int(img.height)
        )

            
    def process_image_from_url(self):
        pass

    def _file_operations(self,file_path:str|Path) -> None:
        pass

    def _create_thumbnail_output(self):
        if not self.thumbnail_output_dir.is_dir():
            self.thumbnail_output_dir.mkdir(exist_ok=True,parents=True)  
    

    def _create_thumbnail(self,image:Image.Image,title) -> Path: # there are some path issues here, fix them
        
        thumbnail = image.copy()
                
        thumbnail.thumbnail((150,150))

        output_dir = Path(self.thumbnail_output_dir)
        output_name = self._create_thumbnail_name()

        output = Path(output_dir/f"{output_name}.webp")
        thumbnail.save(output,"webp",quality=80)
        logger.info("Thumbnail created...")
        return output
        
    def _create_thumbnail_name(self):
        return uuid.uuid4()

    def verify_image(self,file_path:str|Path) -> None:
        if not file_path.is_file():
            raise FileNotFoundError(f"Couldn't find file:{file_path}")
        else:
            with Image.open(file_path) as im:
                im.verify()

        
        

    def _get_file_size(self,file_path:str|Path) -> int:
        file_path = Path(file_path)
        
        size = os.stat(file_path).st_size
        
        return size
            
            






if __name__ == "__main__":

    

    pass
