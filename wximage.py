from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import shutil
import binascii
import threading
from datDictJpg import ruleDictHex


def transFile(dat=b'', srcFile='', desc=''):
    jpgStr = ''
    hex_dat = binascii.b2a_hex(dat)
    for i in range(len(hex_dat) // 2):
        hex_datChar = str(hex_dat[2 * i:2 * (i + 1)], encoding='utf-8')
        hex_jpgChar = ruleDictHex[hex_datChar]
        if hex_jpgChar is not None:
            jpgStr += hex_jpgChar
        else:
            print('DAT character not in rule.')
    jpgBytes = bytes.fromhex(jpgStr)
    srcDir, srcName = os.path.split(srcFile)
    descFile = desc + srcName.replace('.dat', '.jpg')
    with open(descFile, 'wb') as f:
        f.write(jpgBytes)
        print(srcName, u'Conversion successful.')


def openDat(srcFile='', desc=''):
    if os.path.exists(srcFile) is True:
        try:
            with open(srcFile, 'rb') as file:
                dat = file.read()
                transFile(dat=dat, srcFile=srcFile, desc=desc)
        except:
            print('Change Failed !')
    else:
        print('DAT file not exist !')


def datToJpg(src, descDir):
    # openDat(srcFile=src, desc=descDir)
    t = threading.Thread(target=openDat, args=(src, descDir))
    t.start()
    t.join()


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


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.is_directory is False:
            if 'Tiny' in event.src_path:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/Tiny/')
            elif 'send' in event.src_path:
                print('Send file.')
            else:
                copyFile(event.src_path, 'D:/image/weixintemp/dat/')


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "C:/Users/admin/Documents/WeChat Files/xingqitiantsut99/Data", True)
    observer.start()
    print('Observer start.', time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
