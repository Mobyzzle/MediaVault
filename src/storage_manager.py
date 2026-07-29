from pathlib import Path
import shutil
from assets import MediaAsset
import os
from time import sleep

test_path = Path("mediavault_data/testMedia/aaa.webp")
#           Manages Files and Storage
# since we get an Asset, and we will implement an input,download, and Storage folder
# -> ingest file -> processing -> Move original File to new place
#
#
#
class StorageManager:

    def __init__(self, root_dir:Path = Path("mediavault_data")):

        self.root_dir = root_dir
        self.download_dir = root_dir / "downloads"
        self.input_dir = root_dir / "input"
        self.storage_dir = root_dir / "assets"


    def store_file(self,file_path:Path,target_name:str) -> Path:
        """
        Move a processed file into permanent MediaVault Storage

        Args:
            file_path: Path to the staged input file.
            target_name: Unique storage identifier, typically a SHA-256 hash.

        Returns:
            Path to the stored file.
        """
        path = self._check_file_exists(file_path)
        target_dir = self.storage_dir/target_name[:2]
        target_dir.mkdir(exist_ok=True,parents=True)
        return path.rename(target_dir/f"{target_name}{path.suffix}")
        
        
        
        


    def copy_to_input(self,file_path:Path) -> Path:
        self._check_file_exists(file_path=file_path)
        return Path(shutil.copy(file_path,self.input_dir))
        

    def _check_file_exists(self,file_path:Path|str) -> Path:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        else:
            return path


    def initialize(self) -> None:
        self.download_dir.mkdir(exist_ok=True,parents=True)
        self.input_dir.mkdir(exist_ok=True,parents=True)
        self.storage_dir.mkdir(exist_ok=True,parents=True)


if __name__ == "__main__":
    storage = StorageManager()
    storage.initialize()
    new_path = storage.move_to_input(test_path)
    storage.store_file(new_path,"Hello")