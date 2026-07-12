# the actual image class, represents images in the code
# inherits from PIL.Image, but with added data like ID, Source, file_path, etc. etc.
from PIL import Image


class Asset():
    def __init__(self,title:str, file_path:str=None,source_url:str=None):
        self.id = None
        self.title = title
        self.file_path = file_path
        self.source_url = source_url
        self.width = None
        self.height = None
        self.date_added = None
        self.last_viewed = None
        self.viewcount = None
        self.rating = None
        self.favourite = None
        self.thumbnail = None
        



if __name__ == "__main__":
    print("Hello")