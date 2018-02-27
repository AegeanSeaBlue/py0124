import os, shutil

srcf = 'D:/practice/py0124/out.jpg'
descDirc = 'D:/practice/py0124/testf/'

path, name = os.path.split(srcf)
descFile = descDirc + name
copy = shutil.copyfile(srcf, descFile)

print(copy)
