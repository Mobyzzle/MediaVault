# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.
from PIL import Image
import sqlite3
from pathlib import Path
steve_data = {'id': 1, 'title': 'Steve', 'file_path': 'images/Steve.jpg',
               'source_url': None, 'file_size': None, 'width': None, 'height': None, 'date_added': '2026-07-12 20:17:50', 'last_viewed': None,
                 'viewcount': 0, 'rating': 10, 'favourite': 1, 'thumbnail': None}

# implement dataclass later on, typing this out genuinly made me wanna throw the keyboard
class Asset():
    def __init__(self,id:int=None,title:str = None,file_path:str|Path=None,
                 source_url:str|Path=None,width:int=None,height:int=None,
                 date_added:str=None,rating:int=None,favourite:bool|int=None,thumbnail=None,
                 last_viewed:str=None,viewcount:int=None,file_size:int=None):
        self.id = id 
        self.title = title
        self.file_path = file_path
        self.source_url = source_url
        self.width = width
        self.height = height
        self.date_added = date_added
        self.last_viewed = last_viewed
        self.viewcount = viewcount
        self.rating = rating
        self.favourite = favourite
        self.thumbnail = thumbnail
        self.file_size = file_size
        
    @classmethod
    def from_row(cls,data:dict|sqlite3.Row):
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
    steve = Asset.from_row(steve_data)
    