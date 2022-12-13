from pathlib import Path
from os import chdir


path=Path.cwd()
print(path)

path=Path.cwd() /'folder1'
path.mkdir()
print(path)
