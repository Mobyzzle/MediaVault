# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank
from asset import Asset
import logging
from PIL import Image
from pathlib import Path
import os
import uuid
import mimetypes
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


    def save_image(self,source_path:str|Path,output_dir:str|Path,file_name:str) -> None:
        with Image.open(source_path) as img:
            
            file_extension = mimetypes.guess_extension(img.get_format_mimetype())
            
            
            
            img.save(f"{output_dir}/{file_name}{file_extension}")
        

    

    def process_image_from_file(self,asset:Asset) -> Asset: # <-- THIS FOOKIN WORKS HELL FKN YEAH!! good job me c:
        logger.info("Starting to process image...")
        
        
            
        
        self.verify_image(asset)
        with Image.open(asset.file_path) as img:                    # <--- this one checks if it is a file and already throws an exception, no further checking needed
            file_size  = self._get_file_size(asset.file_path)      #   
        
            thumbnail_path = self._create_thumbnail(img)          # change the title to hash later, so thumbnails are unique to each image, and to avoid duplicates    
        
            output = Asset(
                title = str(asset.title),
                file_path=Path(asset.file_path),
                file_size= int(file_size),
                thumbnail_path=Path(thumbnail_path),
                width=int(img.width),
                height=int(img.height),
                source_url=asset.source_url
            )
            logger.info("Succesfully processed Image Data...")
            return output

            


    def _create_thumbnail_output(self):
        if not self.thumbnail_output_dir.is_dir():
            self.thumbnail_output_dir.mkdir(exist_ok=True,parents=True)  
    

    def _create_thumbnail(self,image_object:Image.Image) -> Path: # there are some path issues here, fix them
        
        thumbnail = image_object.copy()
                
        thumbnail.thumbnail((150,150))

        output_dir = Path(self.thumbnail_output_dir)
        output_name = self._create_thumbnail_name()

        output = Path(output_dir/f"{output_name}.webp")
        thumbnail.save(output,"webp",quality=80)
        logger.info("Thumbnail created...")
        return output
        
    def _create_thumbnail_name(self):
        return uuid.uuid4()

    def verify_image(self,asset:Asset) -> None:
        path = asset.file_path
        if not path.is_file():
            raise FileNotFoundError(f"Couldn't find file:{path}")
        else:
            with Image.open(path) as im:
                im.verify()

        
        

    def _get_file_size(self,file_path:str|Path) -> int:
        file_path = Path(file_path)
        
        size = os.stat(file_path).st_size
        
        return size
            
            






if __name__ == "__main__":

    

    pass
