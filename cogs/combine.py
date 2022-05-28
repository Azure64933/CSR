from pathlib import Path
import re
from . import merge, deal_string


def openFile(fileName):
    file_name = fileName[:-4] + "_Comb.txt"
    file_path = './Fin/Combine/' + file_name
    # 判斷有無該myfile.txt檔
    myfile = Path(file_path)
    myfile.touch(exist_ok=True)
    output_txt = open(myfile, 'w')
    return output_txt


def Comb(fileContent, fileName):
    content = fileContent
    output_txt = openFile(fileName)

    merge_content = merge.formated(content)
    output_txt.write(merge_content)

    return len(merge_content)
    output_txt.close()


def third_Comb(fileContent, fileName):
    content = fileContent
    output_txt = openFile(fileName)

    spe_str = ["，", "、", "/", "《", "》", "。", "."
               "「", "」", "：", "；", "【", "】"]
    count_word = 0
    for i in content:
        # 利用spe_str判斷，如果有上述符號便是句子
        for j in spe_str:
            if j in i:
                if i.endswith("。\n") or i.endswith("！\n") or i.endswith("？\n"):
                    output_txt.write(i)
                else:
                    i = re.sub("\\n", "", i)
                    output_txt.write(i)
                break
            elif j == "】":
                output_txt.write(i)

        count_word += len(i)

    return count_word
    output_txt.close()


def new_Comb(fileContent, fileName):
    content = fileContent
    output_txt = openFile(fileName)

    # 先透過merge將文章做初步合併
    merge_content = merge.formated(content)
    # content_list = 將文章以換行為標準，儲存成list
    content_list = merge_content.split("\n")
    spe_str = ["，", "、", "/", "《", "》", "。", "."
               "「", "」", "：", "；", "【", "】"]

    for i in content_list:
        # 去除字串開頭和結尾的空白符
        i = re.sub(r"^\s+|\s+$", "", i)
        # 去除字串中重複的空格/空白符
        i = " ".join(i.split())
        # 利用spe_str判斷，如果有上述符號便是句子
        for j in spe_str:
            if j in i:
                output_txt.write(i + "\n")
                break

    return len(merge_content)
    output_txt.close()


def forth_Comb(fileContent, fileName):
    content = fileContent
    output_txt = openFile(fileName)

    spe_str = ["，", "、", "/", "《", "》", "。", "（", "）"
               "「", "」", "：", "；", "【", "】"]
    count_word = 0

    for i in content:
        # 去除字串開頭和結尾的空白符
        i = re.sub(r"^\s+|\s+$", "", i)
        # 去除字串中重複的空格/空白符
        i = " ".join(i.split())

        # 利用spe_str判斷，如果有上述符號便是句子
        for j in spe_str:
            if j in i:
                if i.endswith("。") or i.endswith("！") or i.endswith("？"):
                    output_txt.write(i + "\n")
                else:
                    output_txt.write(i)
                count_word += len(i)
                break
            elif j == "】":
                output_txt.write(i + "\n")

    return count_word
    output_txt.close()
