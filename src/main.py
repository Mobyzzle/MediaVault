import logging

from vault import Vault

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

    new_asset = iv.ingest_file("Hell yeah",file_path="input/Bigoltiddies.jpg",source_url="https://google.de")

    print(new_asset.__repr__())
    
if __name__ == "__main__":
    main()

