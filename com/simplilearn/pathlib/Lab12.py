from pathlib import Path

path=Path('/Users/om/SB009/com/simplilearn/')
print("*********")

dirs=[ e for e in path.iterdir() if e.is_dir()]
print(dirs)