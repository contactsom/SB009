import os

f=open('SimplilearnLogo.jpeg','rb')
f1=open('NEWSimplilearnLogo.jpeg','wb')

bytes = f.read()
f1.write(bytes)

print("New Image is Created")