import os, re
import pandas as pd
from cogs import segment, combine, merge, deal_string
from pathlib import Path


def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

def test():
    f = open("0523.txt", 'r')
    content = f.readlines()
    print(combine.forth_Comb(content, "0523_comb"))


def test3():
    f = open("Fin\\Combine\\0523__Comb.txt", 'r')
    content = f.readlines()
    segment.third_Seg(content, "0523_seg")


def test_00():
    myfile = "./Fin/00.txt"
    output_txt = open(myfile, 'w')

    f = open("0518.txt", 'r')
    content = f.readlines()
    for i in content:
        i = i.replace("),", "),\n")
        print(i + "-----------------------")
        output_txt.write(i)

    output_txt.close()


def test4():
    i = " 1234  \
        56657"
    # 去除字串開頭和結尾的空白符
    i = re.sub(r"^\s+|\s+$", "", i)
    # 去除字串中重複的空格/空白符
    i = " ".join(i.split())

    print(i)


def test5(str):
    s = str
    lst = s.split(' ')
    new_s = ' '
    print(lst)
    for x in lst:
        if  x.encode( 'UTF-8' ).isalpha():
            new_s += x
            new_s += " "
        else:
            new_s += x

    return new_s

print(test5("的 發 行，以 透 明 string in space\n  test in space測試拉"))

