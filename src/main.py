import logging

from vault import Vault
from database import Database
from processor import Processor
DB_PATH = "database/imagevault.db"
from rich import print


from test_link import link

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


    iv.ingest_from_url("Knight",link,save_to_file=True)
    print("[bold #DF00FF]IF YOU SEE THIS YOUR PIPELINE ACTUALLY WORKS YOU ABSOLUTE MACHINE\nKING, YOU LION\nHERE YOU DROPPED THIS:👑👑👑")
    
if __name__ == "__main__":
    main()

