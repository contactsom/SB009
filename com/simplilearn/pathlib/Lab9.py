from pathlib import Path

path=Path('/usr/local/bin/python3 /Users/om/SB009/com/simplilearn/pathlib/Lab1.py')
print("*********")

print(path)
print(path.as_uri())
print(path.as_posix())
#file:///usr/local/bin/python3%20/Users/om/SB009/com/simplilearn/pathlib/Lab1.py
