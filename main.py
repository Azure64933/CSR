import os
from cogs import segment, combine


comb_word = []
seg_word = []


def openFile(file, mode):
    for fileName in os.listdir(file):
        # mode1 為 comb, mode2 為 seg
        if fileName.endswith(".txt") and mode == 1:
            with open(os.path.join(file, fileName), 'r') as f:
                word = combine.forth_Comb(f.readlines(), fileName)
                comb_word.append(word)
        elif fileName.endswith(".txt") and mode == 2:
            with open(os.path.join(file, fileName), 'r') as f:
                word = segment.third_Seg(f.readlines(), fileName)
                seg_word.append(word)
        else:
            print("非txt檔")


def cal_list(list1, list2):
    for i in range(len(list1)):
        # print("list1: " + str(list1[i]))
        # print("list2: " + str(list2[i]))
        ans = round(float(list2[i]/list1[i]), 2)
        print("cal: " + str(ans))


openFile("CSR_TXT_TEST", 1)
openFile("Fin\\Combine", 2)

print(comb_word)
print(seg_word)
cal_list(comb_word, seg_word)
