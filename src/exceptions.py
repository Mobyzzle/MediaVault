# handling custom Exceptions

# implement pretty rich text later, don't just copy AI code dude
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

import logging

logger = logging.getLogger(__name__)

console = Console()

def not_yet_implemented(Object):
    console.print("[bold red]🚧This feature is not yet Implemented🚧\n{Object}",(Object,))



class AppError(Exception):

    
    def __init__(self,message:str = None, details:str = None):
        self.message = message or self.default_message()
  

        super().__init__(self.message)
    


    def default_message(self) -> str:
        return "Something went wrong."






        