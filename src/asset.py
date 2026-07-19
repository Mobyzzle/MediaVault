# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.

from pathlib import Path
import logging
from dataclasses import dataclass
logger = logging.getLogger(__name__)


    

# this one is much cleaner, once it works, im glad to delete the old shit
@dataclass(slots=True)
class Asset:
    
    title : str                 #           <---- these are are all mandatroy inputs, handled by the processor
    file_path : Path|None = None #  <---These fellas are BOTH technically optional 
    source_url : str|None = None #      but the code throws errors at 2 points of both are missing, so pick one lol



    height : int|None = None                #
    width : int|None = None                 #                   
    file_size : int|None = None             #    
    thumbnail_path : Path|None = None       #


    

    # these are being handled by the Database
    id : int|None = None
    date_added: str|None = None


    rating: int|None = None         #  <--- this one specifically is handled by the database aswell
    favourite: bool = 0     #   they will only become relevant once we have a GUI or some way to display images 
    viewcount: int|None = None      #    none of these are implemented yet
    last_viewed: str|None = None    #


    def __post_init__(self):
        if self.file_path is None and self.source_url is None:
            raise ValueError("file_path and source_url can't both be none, please provide one")



    @classmethod
    def from_row(cls,data:dict):
        return cls(
            id = data["id"],
            title = data["title"],
            file_path = Path(data["file_path"]) if data["file_path"] is not None else None,
            source_url = data["source_url"] or None,
            height = data["height"],
            width = data["width"],
            date_added = data["date_added"] or None,
            file_size = data["file_size"],
            last_viewed = data["last_viewed"] or None,
            viewcount = data["viewcount"] or None,
            rating = data["rating"],
            favourite = bool(data["favourite"]),
            thumbnail_path = Path(data["thumbnail_path"]) if data["thumbnail_path"] is not None else None

        )

    def to_row(self):
        return (
            
            self.title,
            str(self.file_path) if self.file_path is not None else None,
            self.source_url,
            self.height,
            self.width,
            str(self.thumbnail_path) if self.thumbnail_path is not None else None,
            self.file_size,
            self.date_added,
            self.last_viewed,
            self.viewcount,
            self.rating,
            self.favourite,

            self.id,
        )

        
    def path_converter(self):
        if type(self.file_path) is Path:
            return 




if __name__ == "__main__":
    pass