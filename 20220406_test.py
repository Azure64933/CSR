from cogs import merge
from pathlib import Path


input_txt = open('20220406_test.txt', 'r')
content = input_txt.readlines()

# 判斷有無該myfile.txt檔
myfile = Path('./myfile.txt')
myfile.touch(exist_ok=True)
output_txt = open(myfile, 'w')


article = ''
for a in content:
    article += a

lines = article.split("\n")

while '' in lines:
    lines.remove('')


for i in lines:
    if i[0].isdigit():
        output_txt.write(i)
        output_txt.write("\n")
    else:
        output_txt.write(i)

input_txt.close()
output_txt.close()
