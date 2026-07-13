# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.

from sqlite3 import Row
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# implement dataclass later on(maybe in the AssetFactory <.<.), typing this out genuinly made me wanna throw the keyboard
class Asset:
    def __init__(self,id:int=None,title:str = None,file_path:str|Path=None,
                 source_url:str=None,width:int=None,height:int=None,
                 date_added:str=None,rating:int=None,favourite:bool|int=None,thumbnail=None,
                 last_viewed:str=None,viewcount:int=None,file_size:int=None):
        
        if source_url == None and file_path == None:
            raise SyntaxError("source_url and file_path can't be None")
        self.id = id 
        self.title = title

        if not file_path:
            self.file_path = Path("placeholder")
        else:
            self.file_path = Path(file_path)

        self.source_url = source_url
        self.width = width
        self.height = height
        self.date_added = date_added
        self.last_viewed = last_viewed
        self.viewcount = viewcount
        self.rating = rating
        self.favourite = bool(favourite)
        self.thumbnail = thumbnail
        self.file_size = file_size

        logger.debug(f"created an Asset for {self.title}")

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
        
    @classmethod
    def from_row(cls,data:dict|Row):
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
            thumbnail = data["thumbnail"]

        )

if __name__ == "__main__":


    bob_path = Path("images/bob.png")

    bob = Asset(title="Bob",file_path="images/bob.png")
    print(bob.to_row())
    print((bob.file_path))

    
    