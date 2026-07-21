from abc import ABC,abstractmethod
import logging
from pathlib import Path


class Processor(ABC):

    def __init__(self,output_dir:str|Path):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.info(f"Initialized {self.__repr__()}")

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True,exist_ok=True)
        

    
    @abstractmethod
    def process(self):
        pass


            
            
            

