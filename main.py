import os
from cogs import segment, combine, Export

original_name = []
original_word = []
comb_word = []
seg_word = []



def wordCount(filename):
    f = filename.readlines()
    count_word = 0

    for i in f:
        count_word += len(i)

    return count_word


def cal_list(list1, list2):
    cal_Lst = []
    i = 0
    while i < len(list1):
        ans = round(float(list2[i]/list1[i]), 2)
        cal_Lst.append(ans)
        i = i + 1

    return cal_Lst


def openFile(file, mode):
    for fileName in os.listdir(file):
        # mode1 為 comb, mode2 為 seg
        if fileName.endswith(".txt") and mode == 1:
            with open(os.path.join(file, fileName), 'r') as f:
                word = combine.fifth_Comb(f.readlines(), fileName)
                comb_word.append(word)

        elif fileName.endswith(".txt") and mode == 2:
            with open(os.path.join(file, fileName), 'r') as f:
                word = segment.fifth_Seg(f.readlines(), fileName)
                seg_word.append(word)

        elif fileName.endswith(".txt") and mode == 0:
            with open(os.path.join(file, fileName), 'r') as f:
                #把檔案目錄名稱刪除
                original_name.append(f.name[len(file)+2: ])
                original_word.append(wordCount(f))
        else:
            print("非txt檔")


openFile("CSR_TXT_TEST", 0)
openFile("CSR_TXT_TEST", 1)
openFile("Fin\\Combine", 2)

print(original_name)
print(original_word)
print(comb_word)
print(seg_word)
Export.excel_export(original_name, cal_list(original_word, comb_word), cal_list(original_word, seg_word), cal_list(comb_word, seg_word))