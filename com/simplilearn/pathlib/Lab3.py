from pathlib import Path
from os import chdir

path=Path('..')
print(f"Current Directroy : {Path.cwd()}")
chdir(path)
print(f"Current Directroy : {Path.cwd()}")
chdir(path)
print(f"Current Directroy : {Path.cwd()}")