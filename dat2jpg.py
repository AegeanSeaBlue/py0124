import traceback
import binascii

try:
    trans = 'color_trans.dat'
    sheet = 'color_sheet.jpg'

    binfile = open(trans, 'rb')
    a = binfile.read()
    hex_trans = binascii.b2a_hex(a)
    # print(hex_trans)

    binfile = open(sheet, 'rb')
    a = binfile.read()
    hex_sheet = binascii.b2a_hex(a)
    # print(hex_sheet)

    rule = [0] * 256
    flag = [False] * 256
    ruleDict = {}
    ruleDictHex = {}

    for i in range(len(hex_trans) // 2):
        hex_t = hex_trans[2 * i:2 * (i + 1)]
        hex_s = hex_sheet[2 * i:2 * (i + 1)]
        ruleDictHex[str(hex_t, encoding='utf-8')] = str(hex_s, encoding='utf-8')

        int_t = int(hex_t, 16)
        int_s = int(hex_s, 16)

        if flag[int_t] == False:
            rule[int_t] = int_s
            flag[int_t] = True
            ruleDict[int_t] = int_s
        if flag.count(True) == 256:
            break

    print(ruleDict)
    print(ruleDictHex)
    # second convert dat file
    in_file = 'in2.dat'
    out_file = 'out2.jpg'

    binfile = open(in_file, 'rb')
    a = binfile.read()
    binfile.close()
    hex_in = binascii.b2a_hex(a)

    out_ret = ''
    for i in range(len(hex_in) // 2):
        hex_t = hex_in[2 * i:2 * (i + 1)]
        int_t = int(hex_t, 16)
        int_ret = rule[int_t]
        if int_ret > 15:
            hex_ret = hex(int_ret)[2:]
        else:
            hex_ret = '0' + hex(int_ret)[2:]
        out_ret += hex_ret
    hex_file = bytes.fromhex(out_ret)

    binfile = open(out_file, 'wb')
    binfile.write(hex_file)
    binfile.close()
    print(u'转换成功')
except Exception as e:
    print('Exception Info')
    print('-' * 10)
    print('traceback.format_exc():')
    print(traceback.format_exc())
    print('-' * 10)

# input(u'按任意键退出\n')