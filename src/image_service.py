# coordinates the entire image-ingestion pipeline
import sqlite3
import image_database
import image_model
import image_processing
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class ImageService():
    def __init__(self,database:Path|image_database.ImageDatabase):
        
        if not type(database) == image_database.ImageDatabase:
            self.db = image_database.ImageDatabase(database)
            
        else:
            self.db = database
        
        logger.debug("Initialized ImageService...")



    def get_favourites(self,limit:int=1000) -> list[tuple]:
        try:
            self.db.cursor.execute(
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

            return self.db.cursor.fetchall()

        except sqlite3.Error as _e:
            logger.debug(_e)
            return None        