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
    def __init__(self, database_path:str|Path,debugging:bool=False):
        self.database_path = Path(database_path)

        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

        self.debugging = debugging
        if self.debugging:
            self.debug("Successfully connected to Database!")


    def debug(self,text:str,) -> None:
        if self.debugging:
            print(f"[#FF007F]{text}")
        


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
    

    # adding a local image to the databse 
    # implement features for Links, and kwargs later to set favourites and score later on
    def add_image(self,file_path:str|Path,title:str,favourite=0,score=0):
        
        file = Path(file_path)
        if file.is_file():
            try:
                self.cursor.execute(
                    """INSERT INTO images_v2 (
                            title,
                            file_path,
                            favourite,
                            rating)
                        
                        VALUES(
                        ?,?,?,?)""",(title,file_path,favourite,score)
                )
                self.connection.commit()
                self.debug(f"[green]Successfully Uploaded Picture: {self.cursor.lastrowid}/{title}")
                return self.cursor.lastrowid
            except sqlite3.Error as E:
                self.debug(f"[#813E65]Couldn't add Image due to: [underline yellow]{E}")
                return None

            
        
        else:
            self.debug("[red]couldn't find the file :c")
            raise FileNotFoundError(file_path) 
            
    
    def close(self):
        self.connection.close()




if __name__ == "__main__":
    
    DB_PATH = Path("database/imagevault.db")
  
    debug = True
    db = ImageDatabase(DB_PATH,debug)
    

  

    #Testing if the code actually works (it does btw c:)
    

    db.add_image("images/this_file_does_not_exist.jpg","flamingo",score=3)
  
    db.close()