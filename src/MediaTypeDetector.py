import logging
import magic
from pathlib import Path
from enum import Enum
logger = logging.getLogger(__name__)


class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    UNKNOWN = "unknown"



class MediaTypeDetector:
    

    def detect(self,file_path:str|Path) -> MediaType:
        path = Path(file_path)
        if not path.is_file():
            raise FileNotFoundError(f"File not Found: {file_path}")
        
        mime = magic.from_file(str(path),mime=True)
        type_text = mime.split("/")[0]

        if type_text == "image":
            return MediaType.IMAGE
        elif type_text == "video":
            return MediaType.VIDEO
        else:
            return MediaType.UNKNOWN 

    




if __name__ == "__main__":
    detector = MediaTypeDetector()
    print(detector.detect("testMedia/smiley.png").value)
    