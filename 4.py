# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
 

import re

def inRLE (txt):
    csh = 1
    crl = True
    res = ""
    for i in range(len(txt) - 1):
        if txt[i] == txt[i+1]:
            csh += 1
        else:
            res = res + str(csh) + txt[i]
            csh = 1
    if txt[-1] == txt[-2]:
        res = res + str(csh+1) + txt[-1]
    else:
        res = res + "1" + txt[-1]
    return res

def outRLE (txt):
    kef = re.split(r"[A-Za-z]", txt)
    kef.pop(-1)
    pos = 0
    res = ""
    for i in range(len(kef)):
        pos = pos + len(kef[i])
        for j in range(int(kef[i])):
            res = res + txt[pos]
        pos += 1
    return res

fin = open("in.txt")
fout = open("out.txt", "w")
 
fout.write(inRLE(fin.readline()))
fout.write(outRLE(fin.readline()))