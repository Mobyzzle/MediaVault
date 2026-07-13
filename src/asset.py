# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.
from PIL import Image
from sqlite3 import Row
from pathlib import Path


# implement dataclass later on(maybe in the AssetFactory <.<.), typing this out genuinly made me wanna throw the keyboard
class Asset:
    def __init__(self,id:int=None,title:str = None,file_path:str|Path=None,
                 source_url:str|Path=None,width:int=None,height:int=None,
                 date_added:str=None,rating:int=None,favourite:bool|int=None,thumbnail=None,
                 last_viewed:str=None,viewcount:int=None,file_size:int=None):
        self.id = id 
        self.title = title
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


    steve_data = {'id': 1, 'title': 'Steve', 'file_path': 'images/Steve.jpg',
               'source_url': None, 'file_size': None, 'width': None, 'height': None, 'date_added': '2026-07-12 20:17:50', 'last_viewed': None,
                 'viewcount': 0, 'rating': 10, 'favourite': 1, 'thumbnail': None}
    alex_data = dict(steve_data.items())
    alex_data["id"] = 2


    steve = Asset.from_row(steve_data)

    alex = Asset.from_row(alex_data)

    print(steve.to_row(),alex.to_row())
    
    