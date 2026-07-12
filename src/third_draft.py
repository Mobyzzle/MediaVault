import sqlite3
from pathlib import Path
from rich import print

# Notes:
# To-Do: Functions that actually do something, fancy console output using Rich, returning only relevant values,
# Dictionaries for readability  use Python and Pillow to fill in all the extra data and maybe turn it 
#
#


# base class for Python and SQL communication
class ImageDatabase:


    # boilerplate for initiating the Database connection
    def __init__(self, database_path:str):
        self.database_path = Path(database_path)
        
        self.connection = sqlite3.connect(self.database_path)

        self.cursor = self.connection.cursor()



    def get_favourites(self,amount:int=1000) -> list[tuple]:

        self.cursor.execute(
            """
            SELECT
                title,
                file_path,
                rating
            FROM 
                images_v2
            WHERE
                favourite = 1
            ORDER BY
                title
            LIMIT ?;
            """,(amount,)
        )

        return self.cursor.fetchall()
    
    def add_image(self,path:str,title:str="placeholder",*args,**kwargs):

        values1 = args

        print(values1)

        values2 = kwargs
        print(values2.items())

    




        pass


    def close(self):
        self.connection.close()




if __name__ == "__main__":
    
    DB_PATH = Path("database/imagevault.db")

    db = ImageDatabase(DB_PATH)

    print("[#FF44CC]Connected!")

    # Testing if the code actually works (it does btw c:)
    
    print(db.get_favourites())

    db.add_image("file_path","Name",("url","asdjasd"),width=1000,height=1000)


    db.close()