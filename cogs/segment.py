from pathlib import Path
import re
from . import deal_string


def Seg(fileContent, fileName):
    content = fileContent

    file_name = fileName[:-9] + "_Seg.txt"
    file_path = './Fin/Segment/' + file_name
    # 判斷有無該myfile.txt檔
    myfile = Path(file_path)
    myfile.touch(exist_ok=True)
    output_txt = open(myfile, 'w')

    # 將content中的 '\n'字串取出，每段的結尾會變空格
    content_article = ''
    for a in content:
        content_article += a
    lines = content_article.split("\n")

    # 將結尾空格刪除
    # 將結尾是句號且字數大於12的句子保存
    article = ''
    for i in lines:
        if i.endswith(" "):
            i = i.replace(" ", "")
            # print(i+"/")
        if i.endswith("。") and len(i) > 12:
            article += i

    article = article.replace("。", "。\n")
    output_txt.write(article)
    return len(article)

    output_txt.close()


def third_Seg(fileContent, fileName):
    content = fileContent

    file_name = fileName[:-9] + "_Seg.txt"
    file_path = './Fin/Segment/' + file_name
    # 判斷有無該myfile.txt檔
    myfile = Path(file_path)
    myfile.touch(exist_ok=True)
    output_txt = open(myfile, 'w')

    article = ''
    for i in content:
        # count 為句子內 "." 的數量(超過6個......就刪掉)
        count = len(re.findall('\.', i))
        if (i.endswith("。") or i.endswith("。\n") or i.endswith("。 \n")) and len(i) > 12 and count < 4:
            i = deal_string.del_space(i)
            if "。" in i:
                # 每個句號加換行(會多出許多不必要的空行，將其全數刪除)
                i = re.sub("。", "。\n", i)
                i = re.sub(r"^\s+|\s+$", "", i)
                i = " ".join(i.split())
                # 每個句號加換行
                i = re.sub("。", "。\n", i)
                output_txt.write(i)
            else:
                output_txt.write(i)
            article += i

    return len(article)

    output_txt.close()
