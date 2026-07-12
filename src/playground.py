import time
from rich.progress import Progress
from rich.console import Console

out = Console()
out.log("[pink]Initialized Console...")


with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=100)
    
    while not progress.finished:
        progress.update(task1, advance=1)
        time.sleep(0.5)



def asdjksaidkf():
    mystuff = {
        "ready":100,
        "awda":240
    }