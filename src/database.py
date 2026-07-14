# handles transactions between the Database and the Application, knows what is IN the database
# connects to the database directly,
from pathlib import Path
import sqlite3
import logging
from asset import Asset
from rich import print
logger = logging.getLogger(__name__)


class Database:
    def __init__(self,path:str|Path):

        self.path = Path(path)
        
        try:
            self.connection = sqlite3.connect(self.path)
            self.connection.row_factory = sqlite3.Row
     
            
            logger.info("Connected to Database...")

            self.cursor = self.connection.cursor()

            logger.info("Cursor was created....")

        except sqlite3.Error as _e:
            logger.debug("failed to connect to Database due to: %s ",(_e,))
            raise FileNotFoundError



        logger.info("Initialized Database, ready to use")




    def insert_image(self,asset:Asset) -> Asset:

        values = asset.to_row()[0:7] # for insertion we only care about the 7 first values 

        self.cursor.execute(
            """
            INSERT INTO 
                images_v3 (
                title,
                file_path,
                source_url,
                height,
                width,
                thumbnail_path,
                file_size)
            VALUES
                (?,?,?,?,?,?,?)
            """,(values)
        )

        self.connection.commit()


        logger.info("successfully inserted image into Database")
        print("🔥[bold #CC44FF]Congratulations! your Pipeline actually works 🎉🎉🎉🔥")
        return Asset.from_row(self.search_by_id(self.cursor.lastrowid))




    # implement custom queries, and IMPLEMENT THE FUCKING IMAGE OBJECT!!  
    def get_favourites(self,limit:int=1000) -> list[tuple]:
        try:
            self.cursor.execute(
                """
                SELECT
                    title,file_path,source_url,rating
                FROM
                    images_v3
                WHERE 
                    favourite = 1
                ORDER BY title;
                """
            )

            return self.cursor.fetchall()

        except sqlite3.Error as _e:
            logger.exception(_e)
            return None        
    
    def search_by_id(self,id:int) -> Asset:
        try:
            self.cursor.execute(
                """
                SELECT 
                    *
                FROM
                    images_v3
                WHERE
                    id = ?;
                """,(id,)
            )

            return self.cursor.fetchone()

        except sqlite3.Error as _e:
            logger.exception("An Error occured: %s",(_e,))
            raise sqlite3.DataError from _e