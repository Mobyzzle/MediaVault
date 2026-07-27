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
    asset = iv.ingest_from_url("Big ol Bitties","https://static1.e621.net/data/sample/fb/a2/fba206e404425e1984be5d90deae8f1d.webp",True)
    print(asset.__repr__())
    
if __name__ == "__main__":
    main()

