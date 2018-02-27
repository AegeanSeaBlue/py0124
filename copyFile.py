import os
import shutil
import time


def copyFile(src, descDir):
    srcPath, fileName = os.path.split(src)
    descPath = descDir + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '_' + fileName
    shutil.copy(src, descPath)
