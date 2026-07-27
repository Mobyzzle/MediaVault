from pathlib import Path
import shutil
from assets import MediaAsset

test_path = "mediavault_data/assets/test.jpg"
#           Manages Files and Storage
# since we get an Asset, and we will implement an input,download, and Storage folder
# -> ingest file -> processing -> Move original File to new place
#
#
#
class StorageManager():

    def __init__(self, root_dir:Path = Path("mediavault_data")):

        self.root_dir = root_dir
        self.DOWNLOAD_DIR = root_dir / "downloads"
        self.INPUT_DIR = root_dir / "input"
        self.STORAGE_DIR = root_dir / "assets"


    def store_file(self,file_path:Path) -> None:
        if not file_path.exists():
            raise ValueError(f"File not found: {file_path}")


    def move_to_input(self,file_path:Path) -> None:
        self._check_file_exists(file_path=file_path)
        shutil.copy(file_path,self.INPUT_DIR)
        

    def _check_file_exists(self,file_path:Path|str) -> None:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        else:
            return path


    def initialize(self) -> None:
        self.DOWNLOAD_DIR.mkdir(exist_ok=True,parents=True)
        self.INPUT_DIR.mkdir(exist_ok=True,parents=True)
        self.STORAGE_DIR.mkdir(exist_ok=True,parents=True)


if __name__ == "__main__":
    storage = StorageManager()
    storage.initialize()
    storage.move_to_input(test_path)