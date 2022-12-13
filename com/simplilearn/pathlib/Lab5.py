from pathlib import Path
from shutil import copyfile

sourse=Path('employee.txt')
destination=Path('employeeNew.txt')
copyfile(sourse,destination)
