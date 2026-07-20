import logging
from rich.logging import RichHandler
from vault import Vault

DB_PATH = "database/imagevault.db"
from rich import print


from test_link import link

def configure_logging(debug:bool = True) -> None:
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[RichHandler(markup=True)]
    )


def main():
    test_image = "test_image/bob.png"
    
    #  logging boilerplate, we will customize this later 
    configure_logging()
    logging.info("Starting Imagevault....")

    iv = Vault(DB_PATH)

    image_asset = iv.ingest_file("Hell yeah",file_path="input/test.jpg",source_url="https://google.de")
    url_asset = iv.ingest_from_url("Even more Hell yeah",source_url="https://cdn.waifu.im/8059.jpg",save_to_file=True)
    print(image_asset.__repr__())
    print(url_asset.__repr__())
    
if __name__ == "__main__":
    main()

