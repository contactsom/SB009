from pathlib import Path

path=Path('/Users/om/SB009/com/simplilearn/')
print("*********")

for e in path.rglob('*.py'):
    print(e)

print("----- TXT File")
for e in path.rglob('*.txt'):
    print(e)