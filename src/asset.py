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
    height : int                #
    width : int                 #                   
    file_size : int             #    
    thumbnail_path : Path       #


    file_path : Path|None = None #  <---These fellas are BOTH technically optional 
    source_url : str|None = None #      but the code throws errors at 2 points of both are missing, so pick one lol

    # these are being handled by the Database
    id : int|None = None
    date_added: str|None = None


    rating: int|None = None         #  <--- this one specifically is handled by the database aswell
    favourite: bool|None = None     #   they will only become relevant once we have a GUI or some way to display images 
    viewcount: int|None = None      #    none of these are implemented yet
    last_viewed: str|None = None    #


    #@classmethod
    def __post_init__(self):
        if self.file_path is None and self.source_url is None:
            raise ValueError("file_path and source_url can't both be none, please provide one")

    @classmethod
    def from_row(cls,data:dict):
        return cls(
            id = int(data["id"]),
            title = str(data["title"]),
            file_path = Path(data["file_path"]),
            source_url = str(data["source_url"]),
            height = int(data["height"]),
            width = int(data["width"]),
            date_added = str(data["date_added"]),
            file_size = int(data["file_size"]),
            last_viewed = str(data["last_viewed"]),
            viewcount = int(data["viewcount"]),
            rating = int(data["rating"]),
            favourite = int(data["favourite"]),
            thumbnail_path = Path(data["thumbnail_path"])

        )

    def to_row(self):
        return (
            
            str(self.title),
            str(self.file_path),
            str(self.source_url),
            int(self.height),
            int(self.width),
            str(self.thumbnail_path),
            int(self.file_size),
            str(self.date_added),
            str(self.last_viewed),
            int(self.viewcount),
            int(self.rating),
            bool(self.favourite),

            int(self.id),
        )

        





if __name__ == "__main__":
    pass