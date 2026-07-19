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
                (
                :title,
                :file_path,
                :source_url,
                :height,
                :width,
                :thumbnail_path,
                :file_size)
            """,{
                "title":asset.title,
                "file_path":str(asset.file_path),               #   <----- these two need to be strings when inserted
                "source_url":asset.source_url,                  #
                "height" : asset.height,                        #
                "width":asset.width,                            #
                "thumbnail_path":str(asset.thumbnail_path),     #   <----- into the database, they are return back into Path object in the Asset constructor
                "file_size":asset.file_size

            }
        )

        self.connection.commit()


        logger.info("successfully inserted image into Database")
        
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

            output = self.cursor.fetchone()
            if output is None:
                raise ValueError("No entry matching this ID found")
            return output
        except sqlite3.Error:
            logger.debug("Failed Database Search")
            raise