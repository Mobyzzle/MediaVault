# processess and validates images that are put in into an imageIV object, creates thumbnail, reads data, makes the object ready to push into the databank

import logging
from PIL import Image
from pathlib import Path
import os
import uuid
import mimetypes
import math
from .base_processor import Processor
import hashlib
logger = logging.getLogger(__name__)


class ImageProcessor(Processor):
    # add to this when you learn about new aspect ratios
    STANDARD_RATIOS = (
        (1, 1),   # Square (Instagram)
        (4, 5),   # Portrait (Instagram)
        (3, 4),   # Standard Photo
        (2, 3),   # Classic Photo (DSLR / 35mm)
        (9, 16),  # Mobile Story / Video
        (16, 9),  # Widescreen
        (21, 9)   # Ultrawide
        )
    
    def __init__(self,thumbnail_output:str|Path):
        super().__init__(thumbnail_output)
        
        self.logger.info("Initialized ImageProcessor...")


        



    def _get_image_from_file(self,file_path:str|Path) -> Image.Image:
        
        path = Path(file_path)

        with Image.open(path) as im:
            self.logger.info("Image opened...")
            im.load()
            return im.copy()


    def save_image(self,source_path:str|Path,output_dir:str|Path,file_name:str) -> None:
        with Image.open(source_path) as img:
            
            file_extension = mimetypes.guess_extension(img.get_format_mimetype())
            
            img.save(f"{output_dir}/{file_name}{file_extension}")
        

   

    def process(self,file_path:Path,title:str,source_url:str=None) -> dict: # <-- THIS FOOKIN WORKS HELL FKN YEAH!! good job me c:
        self.logger.info("Starting to process image...")
        
        self._verify_image(file_path)  # <--- this one checks if it is a file and already throws an exception, no further checking needed
        file_hash = self._get_file_hash(file_path)
        with Image.open(file_path) as img:                   
            file_size  = self._get_file_size(file_path)      #
        
            thumbnail_path = self._create_thumbnail(img,file_hash)          # change the title to hash later, so thumbnails are unique to each image, and to avoid duplicates    
            aspect_ratio = self._calculate_aspect_ratio(img.width,img.height)
            output = {
                "title":title,
                "file_path":Path(file_path),
                "file_size": int(file_size),
                "thumbnail_path":Path(thumbnail_path),
                "width":int(img.width),
                "height":int(img.height),
                "aspect_ratio":aspect_ratio,
                "source_url":source_url,
                "file_hash":file_hash
            }
            self.logger.info("Succesfully processed Image Data...")
            return output

            



    

    def _create_thumbnail(self,image_object:Image.Image,file_hash:str) -> Path: # there are some path issues here, fix them
        
        thumbnail = image_object.copy()
                
        thumbnail.thumbnail((500,500))

        output_dir = self.output_dir
        output_name = file_hash

        output = Path(output_dir/f"{output_name}.webp")
        thumbnail.save(output,"webp",quality=80)
        self.logger.info("Thumbnail created...")
        return output
        
    def _create_thumbnail_name(self):
        return uuid.uuid4()
    
    def _calculate_aspect_ratio(self,width:int,height:int) -> str:

        output = None   # just an object to format the output on different endpoints

        

        # calculate the actual Aspect Ratio in whole numbers
        gcd = math.gcd(width,height)
        ratio_width = width // gcd
        ratio_height = height // gcd

        if ratio_width < 20 and ratio_height < 20:   # <-- if the weird numbers are not too weird, fuck it output them
            output = f"{ratio_width}:{ratio_height}" 
        else:
            target_ratio = width/height  # <--- actual aspect ratio as a decimal, i thought it might be simpler from here on out HAHHAHAHAHAHAHAHAHHAHAHAHA
            best_difference = float("inf") # <- placeholder value, literally everything is smaller than infinity

            #actual logic for calculating, and storing the smallest difference to an actual aspect ratio
            for standart_width, standart_height in self.STANDARD_RATIOS:
                

                absolute_difference = abs(target_ratio-(standart_width/standart_height))

                # if the difference is smaller than the best, update the best and save the state
                if absolute_difference < best_difference:
                    best_difference = absolute_difference
                    output = f"{standart_width}:{standart_height}"

        return output  


    def _verify_image(self,file_path:Path) -> None:

        if not file_path.is_file():
            raise FileNotFoundError(f"Couldn't find file:{file_path}")
        
        with Image.open(file_path) as im:
            im.verify()

        
        

    def _get_file_size(self,file_path:Path) -> int: 

        size = os.stat(file_path).st_size  
        return size
            
            

    def _get_file_hash(self,file_path:Path) -> str:
        with open(file_path,"rb") as file:
            digest = hashlib.file_digest(file,"sha256")
            return digest.hexdigest()




if __name__ == "__main__":

    proc = ImageProcessor("DELETE_ME")
    data = proc.process(Path("testMedia/bob.png"))
    print(data)
    pass
