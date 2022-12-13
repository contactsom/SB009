from pathlib import Path
from shutil import copyfile

path=Path.home()
print(path)


doc=path / 'Documents'
print(doc)

pic=path / 'Picture'
print(pic)