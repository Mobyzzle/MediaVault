from dataclasses import dataclass
from abc import ABC,abstractmethod
from __future__ import annotations
import logging
from pathlib import Path
logger = logging.getLogger(__name__)


@dataclass 
class MediaAsset(ABC):            # Base Asset class
    title:str                       # these are all actually whats needed
    file_path: Path | None = None          #
    source_url:str|None = None           # 


    @classmethod
    @abstractmethod
    def from_data(cls,data:dict) -> MediaAsset:
        pass

    @classmethod
    @abstractmethod
    def from_row(cls,data:dict) -> MediaAsset:
        pass


    @abstractmethod
    def to_row(self) -> dict:
        pass

    



    def __post_init__(self):
        if self.file_path is None and self.source_url is None:
            raise ValueError("File Path and Source Url can't both be None, please provide one")