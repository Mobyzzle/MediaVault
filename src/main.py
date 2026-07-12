import logging

import vault 
from database import Database

DB_PATH = "database/imagevault.db"

def configure_logging(debug:bool = True) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )


def main():

    # logging boilerplate, we will customize this later 
    configure_logging()
    logging.info("Starting Imagevault....")

    iv = Database(DB_PATH)

    fav = iv.get_favourites()

    print(fav)

if __name__ == "__main__":
    main()

