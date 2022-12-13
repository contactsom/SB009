from pathlib import Path

path=Path('/Users/om/SB009/com/simplilearn/pathlib/Lab1.py')
print("*********")

print(f"The Part is : {path.parts}")
print(f"The Drive is : {path.drive}")
print(f"The Root is : {path.root}")
print("-----------------------------")
print(f"The Name is : {path.name}")
print(f"The stem is : {path.stem}")
print(f"The Anchor is : {path.anchor}")