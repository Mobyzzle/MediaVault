import sqlite3
from pathlib import Path
from rich import print
from rich_gradient import Text

# boiler plate initiation to reuse later
DATABASE_PATH = Path("database/imagevault.db")

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()



def get_favourites(cursor:sqlite3.Cursor) -> list[tuple]:
    cursor.execute(
        """
        SELECT
            title,
            file_path,
            rating
        FROM
            images_v2
        WHERE
            favourite = 1
        ORDER BY rating DESC;
        """
    )

    rows = cursor.fetchall()
    return rows



def get_images_by_rating(cursor:sqlite3.Cursor,minimum_rating:int) -> list:
    cursor.execute(
        """
        SELECT
            title,
            rating,
            file_path
        FROM
            images_v2
        WHERE
            rating >= ?
        ORDER BY rating DESC;
        """,(minimum_rating,)
    )    
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    favs = get_favourites(cursor)
    ratings = get_images_by_rating(cursor,2)
    
    print(favs,ratings)

    