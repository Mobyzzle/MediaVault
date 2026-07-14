import logging

from vault import Vault
from database import Database
from processor import Processor
DB_PATH = "database/imagevault.db"

def configure_logging(debug:bool = True) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )


def main():
    test_image = "test_image/bob.png"
    
    #  logging boilerplate, we will customize this later 
    configure_logging()
    logging.info("Starting Imagevault....")

    iv = Vault(DB_PATH)

    im = iv.add_image("bob",test_image)
    print(im.to_row())
if __name__ == "__main__":
    main()

