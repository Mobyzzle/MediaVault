import logging

from vault import Vault
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

    iv = Vault(DB_PATH)

    iv.add_image()
if __name__ == "__main__":
    main()

