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

    im = iv.ingest_file("bob",test_image)
    print(im)
    print("🔥[bold #CC44FF]Congratulations! your Pipeline actually works 🎉🎉🎉🔥")
    iv.ingest_from_url("Knight",link)
if __name__ == "__main__":
    main()

