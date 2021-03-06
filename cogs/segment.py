from pathlib import Path
import re
from . import deal_string, combine


def openFile(fileName, filePath):
    file_name = fileName[:-9] + "_Seg.txt"
    print("SegFileName:", file_name)
    file_path = './Fin/Segment/' + filePath + "/" + file_name
    print("SegFilePath:", file_path)
    # 判斷有無該myfile.txt檔
    myfile = Path(file_path)
    myfile.touch(exist_ok=True)
    output_txt = open(myfile, 'w')
    return output_txt


def fifth_Seg(fileContent, fileName, filePath):
    output_txt = openFile(fileName, filePath)

    recomb_content = combine.Comb(fileContent)
    content = recomb_content.split('\n')

    article = ''
    for i in content:
        # count 為句子內 "." 的數量(超過6個......就刪掉)
        count = len(re.findall('\.', i))
        if (i.endswith("。") or i.endswith("。\n") or i.endswith("。 \n")) and len(i) > 12 and count < 7:
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
