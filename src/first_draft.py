import sqlite3
from pathlib import Path
from rich import print
from rich_gradient import Text



print(Text("""██╗███╗   ███╗ █████╗  ██████╗ ███████╗██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
██║██╔████╔██║███████║██║  ███╗█████╗  ██║   ██║███████║██║   ██║██║     ██║
██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║
██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗ ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║
╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝""",colors=["#CCFF00","#FF00A5"],justify="left"))

DATABASE_PATH = Path("database/imagevault.db")

print(f"[green]{DATABASE_PATH}")


connection = sqlite3.connect(DATABASE_PATH)

print("[magenta]Connected to [dark_green]Database")



cursor = connection.cursor()

cursor.execute(
    """
    SELECT
        title,
        file_path
    FROM images_v2
    WHERE
        favourite = 1
    ORDER BY rating DESC;
    """
)

rows = cursor.fetchall()

print(f"[orange_red1]There were {len(rows)} Items found")

for row in rows:
    print(f"[blue]{row}")



connection.close()
print("[magenta]Connection[red] Closed")