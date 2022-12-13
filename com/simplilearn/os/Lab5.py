from zipfile import *

f=ZipFile("simp.zip",'w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('abd.txt')
f.write('abe.txt')
f.write('abf.txt')
f.close()
