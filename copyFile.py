import os
import shutil
import time


def copyFile(src, descDir):
    try:
        srcPath, fileName = os.path.split(src)
        print(fileName)
        descPath = descDir + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '_' + fileName
        shutil.copy(src, descPath)
    except:
        print('Copy DAT Failed!')
        pass
