# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.

from pathlib import Path
import logging
from dataclasses import dataclass
logger = logging.getLogger(__name__)

# implement dataclass later on(maybe in the AssetFactory <.<.), typing this out genuinly made me wanna throw the keyboard
class AssetOLD:
    def __init__(self,id:int=None,title:str = None,file_path:str|Path=None,
                 source_url:str=None,width:int=None,height:int=None,
                 date_added:str=None,rating:int=1,favourite:bool|int=None,thumbnail=None,
                 last_viewed:str=None,viewcount:int=None,file_size:int=None):
        
        if source_url == None and file_path == None:
            raise SyntaxError("source_url and file_path can't be None")
        if rating is not None and not 1 <= rating <= 10:
            raise ValueError(f"rating must be 1-10, got {rating}")
        self.id = id # created automatically
        self.title = title # user input, necessary

        if not file_path:
            self.file_path = Path("placeholder")  # user input, only necessary when no url is given, url currently not implemented
        else:                                     # also make this more pretty and readable in the future, i coded this and i dont even fkn know what it does :^)
            self.file_path = Path(file_path)

        self.source_url = source_url # user input, necessary if no path is given
        self.width = width # automatically calculated
        self.height = height # automacially calculated
        self.date_added = date_added # Database handles this automatically, maybe make python do it later for more control
        self.last_viewed = last_viewed # Database Class handles this, created when image is viewed or downloaded, not implemented yet
        self.viewcount = viewcount # another one for the Database Class, not implemented yet


        self.rating = rating # user input, not necessary, later implement max ranges
        
        
        self.favourite = bool(favourite) # user input, not necessary, but its fun
        self.thumbnail = thumbnail # Processor generates and saves in thumbnail directory, implemented
        self.file_size = file_size # another for the Processor, not implemented yet

        logger.debug(f"created an Asset for {self.title}") # also remove this shit and write your own logger with Rich, make it pretty ABSOLUTE PRIORITY

    def to_row(self) -> dict[str,object]:

        return {
            "id": self.id,
            "title":self.title,
            "file_path" : Path(self.file_path),
            "source_url": self.source_url,
            "width" : self.width,
            "height": self.height,
            "date_added" : self.date_added,
            "last_viewed" : self.last_viewed,
            "viewcount" : self.viewcount,
            "rating" : self.rating,
            "favourite" : self.favourite,
            "thumbnail" : self.thumbnail,
            "file_size" : self.file_size
            
        }

        pass
        
    
    

# this one is much cleaner, once it works, im glad to delete the old shit
@dataclass(slots=True)
class Asset:
    
    title : str
    height : int
    width : int
    file_size : int
    thumbnail_path : Path


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
            id = data["id"],
            title = data["title"],
            file_path = data["file_path"],
            source_url = data["source_url"],
            height = data["height"],
            width = data["width"],
            date_added = data["date_added"],
            file_size = data["file_size"],
            last_viewed = data["last_viewed"],
            viewcount = data["viewcount"],
            rating = data["rating"],
            favourite = data["favourite"],
            thumbnail_path = data["thumbnail_path"]

        )

    def to_row(self):
        return (
            
            self.title,
            str(self.file_path),
            self.source_url,
            self.height,
            self.width,
            str(self.thumbnail_path),
            int(self.file_size),
            self.date_added,
            self.last_viewed,
            self.viewcount,
            self.rating,
            self.favourite,

            self.id,
        )

        





if __name__ == "__main__":
    pass