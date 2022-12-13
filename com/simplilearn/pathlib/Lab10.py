from pathlib import Path

path=Path('/Users/om/SB009/com/simplilearn/pathlib/Lab1.py')
print("*********")
home=path.home()
print(home)


relative=path.relative_to(home)
print(relative)