import os
import shutil
import time
from datToJpg import datToJpg


def copyFile(src, descDir):
    try:
        srcPath, fileName = os.path.split(src)
        print('Copy file',fileName)
        descPath = descDir + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '_' + fileName
        shutil.copy(src, descPath)
        if ('Tiny' in src) is False:
            datToJpg(descPath, 'D:/image/weixintemp/image/')
    except:
        print('Copy DAT Failed!')
        pass
