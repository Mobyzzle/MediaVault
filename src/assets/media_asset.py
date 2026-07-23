from __future__ import annotations
from dataclasses import dataclass
from abc import ABC,abstractmethod
import logging
from pathlib import Path
from ..enums import MediaType
logger = logging.getLogger(__name__)


@dataclass(slots=True) 
class MediaAsset(ABC):            # Base Asset class
    title:str  
    media_type: MediaType                     # these are all actually whats needed
    file_path: Path | None = None          #
    source_url:str|None = None           # 
            # this gets added during processing

    

    



    def __post_init__(self):
        if self.file_path is None and self.source_url is None:
            raise ValueError("File Path and Source Url can't both be None, please provide one")