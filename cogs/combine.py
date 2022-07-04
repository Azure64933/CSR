from pathlib import Path
import re


def openFile(fileName, filePath):
    file_name = fileName[:-4] + "_Comb.txt"
    file_path = './Fin/Combine/' + filePath + "/" + file_name
    # 判斷有無該myfile.txt檔
    myfile = Path(file_path)
    myfile.touch(exist_ok=True)
    output_txt = open(myfile, 'w')
    return output_txt


def Comb(content):
    return_content = ''
    spe_str = ["，", "、", "/", "《", "》", "。", "（", "）",
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
                    return_content += i + "\n"
                else:
                    return_content += i
                count_word += len(i)
                break
            elif j == "】":
                return_content += i + "\n"

    return return_content


def fifth_Comb(fileContent, fileName, filePath):
    content = fileContent
    output_txt = openFile(fileName, filePath)

    i = Comb(content)

    output_txt.write(i)

    return len(i)
    output_txt.close()
