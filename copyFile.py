import os
import shutil
import time
from datToJpg import datToJpg


def copyFile(src, descDir):
    try:
        srcPath, fileName = os.path.split(src)
        # descPath = descDir + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '_' + fileName
        descPath = descDir + fileName
        shutil.copy(src, descPath)
        print('Copy', fileName)
        if 'Tiny' not in src:
            datToJpg(descPath, 'D:/image/weixintemp/image/')
    except:
        print('Copy DAT Failed!')
        pass
