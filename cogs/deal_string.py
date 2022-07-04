import re

# 检验是否含有且出過10個中文字符


def is_contains_chinese(strs):
    str_num = 0
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            str_num += 1
        if str_num >= 10:
            return True
    return False

# 检验是否全是中文字符


def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

#   s:一段話  ; c = 句子中特定字符


def get_position(s, c):
    sentence = s
    clear_string = c
    lst = []
    for pos, char in enumerate(sentence):
        if(char == clear_string):
            lst.append(pos)
    return lst


def get_space_index(sentence):
    s = sentence
    # 取得字串中空格的位置
    lst = get_position(sentence, ' ')
    # 取得字串中"英文"與"多重空格"空格的位置
    lst_space = get_position(sentence, ' ')

    # 修改lst_space(去掉英文相接的空格)
    # x 為 int(數值)
    for x in lst:
        pre_str = sentence[x-1]
        next_str = sentence[x+1]
        # 判斷空格位置前後的char是否同為英文或中文
        if(char_isSame(pre_str, next_str)):
            if (is_all_chinese(pre_str) and is_all_chinese(next_str)):
                lst_space.remove(x)
        elif(pre_str.isspace()):
            lst_space.remove(x)

    return s


def del_space(str):
    s = str
    lst = s.split(' ')
    new_s = ''
    for x in lst:
        # 只判斷該字串最後一個字元是否為英文，是英文的話就用空格接起
        if x[-1:].encode('UTF-8').isalpha() or x[-1:].isdigit():
            new_s += x
            new_s += " "
        else:
            new_s += x

    return new_s
