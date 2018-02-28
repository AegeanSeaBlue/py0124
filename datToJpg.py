import os
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
    t = threading.Thread(target=openDat, args=(src, descDir))
    t.start()
