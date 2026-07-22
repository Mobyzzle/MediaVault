# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.
from __future__ import annotations
from pathlib import Path
import logging
from dataclasses import dataclass
logger = logging.getLogger(__name__)
from .media_asset import MediaAsset

    

# this one is much cleaner, once it works, im glad to delete the old shit
@dataclass(slots=True)
class ImageAsset(MediaAsset):
    
    

    # these are Image specific now, the base class doesn't need these
    height : int|None = None                #
    width : int|None = None                 #                   
    file_size : int|None = None             #    
    thumbnail_path : Path|None = None       #
    aspect_ratio: str|None = None

    

    # these are being handled by the Database
    id : int|None = None
    date_added: str|None = None
    rating: int|None = None         #  <--- this one specifically is handled by the database aswell
    favourite: bool = 0     #   they will only become relevant once we have a GUI or some way to display images 
    viewcount: int|None = None      #    
    last_viewed: str|None = None    #
    file_hash: str|None = None         # <--- implement this once the backend and pipeline are working again


        
    




if __name__ == "__main__":
    print("you are cute")