#!/usr/bin/python
import sys

def shift(l , n):
    return l[n:] + l[:n]

def encrypt(fi, fo, key1, key2, key3):
    while True:
        ostr = fi.read(key1)
        if not ostr:
            break
        lis = list(ostr)
        lis2 = []
        for i in lis:
            lis2.append(chr(ord(i) + key2))
        wstr = ''.join(shift(lis2, key3))
        fo.write(wstr)
    return

def decrypt(fi, fo, key1, key2, key3):
    while True:
        ostr = fi.read(key1)
        if not ostr:
            break
        lis = list(ostr)
        lis2 = []
        for i in lis:
            lis2.append(chr(ord(i) - key2))
        wstr = ''.join(shift(lis2, 0 - key3))
        fo.write(wstr)
    return



if __name__ == "__main__":
    fi = open(sys.argv[1], 'r')
    fo = open(sys.argv[2], 'w')
    key1 = int(sys.argv[3])
    key2 = int(sys.argv[4])
    key3 = int(sys.argv[5])
    what = sys.argv[6]
    if what == 'e':
        encrypt(fi, fo, key1, key2, key3)
    if what == 'd':
        decrypt(fi, fo, key1, key2, key3)
    fi.close()
    fo.close()

