# handles transactions between the Database and the Application, knows what is IN the database
# connects to the database directly,
from pathlib import Path
import sqlite3
import logging

logger = logging.getLogger(__name__)


class ImageDatabase():
    def __init__(self,path:str|Path):

        self.path = Path(path)
        
        try:
            self.connection = sqlite3.Connection(self.path)
            
            logger.info("Connected to Database...")

            self.cursor = self.connection.cursor()

            logger.info("Cursor was created....")

        except sqlite3.Error as _e:
            logger.debug("failed to connect to Database due to: %s ",(_e,))



        logger.debug("Initialized ImageDatabase, ready to use")
        

    def get_favourites(self,limit:int=1000) -> list[tuple]:
        try:
            self.cursor.execute(
                """
                SELECT
                    title,file_path,source_url
                FROM
                    images_v3
                WHERE 
                    favourite = 1
                ORDER BY title;
                """
            )

            return self.cursor.fetchall()

        except sqlite3.Error as _e:
            logger.debug(_e)
            return None    