import logging
from rich.logging import RichHandler
from vault import Vault


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
    
    #  logging boilerplate, we will customize this later 
    configure_logging()
    logging.info("Starting Imagevault....")

    iv = Vault()

    image_asset = iv.ingest_file("Hell yeah",file_path="images/Panda.jpg")
    print(image_asset)
    print(type(image_asset))

    
if __name__ == "__main__":
    main()

