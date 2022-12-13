import collections
from pathlib import Path

docs= Path.home() / 'SB009/com/simplilearn/pathlib'

#docs=Path('/Users/om/SB009/com/simplilearn/')
print("*********")

files = [path.suffix for path  in docs.iterdir() if path.is_file() and path.suffix]
data = collections.Counter(files)
print(data)

for key , value in data.items():
    print(f'{key}: {value}')