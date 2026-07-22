# handles transactions between the Database and the Application, knows what is IN the database
# connects to the database directly,
from pathlib import Path
import sqlite3
import logging
from assets import MediaAsset,ImageAsset
from enums import MediaType
logger = logging.getLogger(__name__)


class MediaRepository:
    def __init__(self,path:str|Path):

        self.path = Path(path)

        self.TABLE = "images_v5"
        
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




    def insert_asset(self,asset:MediaAsset) -> dict:

        row = self._convert_to_row(asset)

        self.cursor.execute(
            f"""
            INSERT INTO 
                {self.TABLE} (
                title,
                file_path,
                source_url,
                height,
                width,
                thumbnail_path,
                file_size,
                aspect_ratio,
                file_hash,
                media_type)
            VALUES
                (
                :title,
                :file_path,
                :source_url,
                :height,
                :width,
                :thumbnail_path,
                :file_size,
                :aspect_ratio,
                :file_hash,
                :media_type
                )
            """,{
                "title":row["title"],
                "file_path":row["file_path"],               #   <----- these two need to be strings when inserted
                "source_url":row["source_url"],                  #
                "height" : row["height"],                        #
                "width":row["width"],                            #
                "thumbnail_path":row["thumbnail_path"],     #   <----- into the database, they are return back into Path object in the Asset constructor
                "file_size":row["file_size"],
                "aspect_ratio":row["aspect_ratio"],
                "file_hash":row["file_hash"],
                "media_type":row["media_type"]
            }
        )

        self.connection.commit()


        logger.info("successfully inserted image into Database")

        
        return self.search_by_id(self.cursor.lastrowid) 




    # implement custom queries, and IMPLEMENT THE FUCKING IMAGE OBJECT!!  
    def get_favourites(self,limit:int=10) -> list[dict]:
        try:
            self.cursor.execute(
                f"""
                SELECT
                    title,file_path,source_url,rating
                FROM
                    {self.TABLE}
                WHERE 
                    favourite = 1
                LIMIT ?
                ORDER BY title;
                """,(limit,)
            )

            favourite_rows =  self.cursor.fetchall()
            favourite_dicts = []
            for row in favourite_rows:
                favourite_dicts.append(dict(row))
            return favourite_dicts

        except sqlite3.Error as _e:
            logger.exception(_e)
            return None        
    
    def search_by_id(self,id:int) -> dict:
        try:
            self.cursor.execute(
                f"""
                SELECT 
                    *
                FROM
                    {self.TABLE}
                WHERE
                    id = ?;
                """,(id,)
            )

            output = dict(self.cursor.fetchone())
            logger.debug(f"Query found {output}")
            if output is None:
                raise ValueError("No entry matching this ID found")
            return output
        except sqlite3.Error:
            logger.debug("Failed Database Search")
            raise

    def _convert_to_row(self,asset:MediaAsset) -> dict:
        match asset.media_type:
            case MediaType.IMAGE:
                return self._convert_imageasset_to_row(asset)
            


    def _convert_imageasset_to_row(self,asset:ImageAsset) -> dict:
        return {
            "media_type" : asset.media_type,
            "title":asset.title,
            "file_path":str(asset.file_path) if asset.file_path is not None else None,               #   <----- these two need to be strings when inserted
            "source_url":str(asset.source_url) if asset.source_url is not None else None,            #
            "height" : asset.height,                        #
            "width":asset.width,                            #
            "thumbnail_path":str(asset.thumbnail_path) if asset.thumbnail_path is not None else None,     #   <----- into the database, they are return back into Path object in the Asset constructor
            "file_size":asset.file_size,
            "aspect_ratio":asset.aspect_ratio,
            "file_hash":asset.file_hash,
            "media_type":asset.media_type.value,
        }
