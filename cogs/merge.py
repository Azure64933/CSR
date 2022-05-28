# cogs/merge.py

def isEndOfP(line):
        notendstrs = ["www.", "文章"]
        for notendstr in notendstrs:
            if line.endswith(notendstr):
                return False
        endstrs = ["\"", ".", "”", "。", "！", "？", "!", "?", "……", "…", "》", "：", ":", ";", "；", "1", "2", "3",
                   "4", "5", "6", "7", "8", "9", "0", "章", "部", "碌", "著", "譯", "言", "~", "---", "」"]
        for endstr in endstrs:
            if line.endswith(endstr):
                return True
        return False

def isStrD(line):
        strDa = ["\"", "(", "{", "[", "《", "“", "‘", "（", "{", "【"]
        strDb = ["\"", ")", "}", "]", "》", "”", "’", "）", "}", "】"]
        for i in range(0, len(strDa)):
            if countSubString(line, strDa[i]) != countSubString(line, strDb[i]):
                return False
        return True

def countSubString(line, substr):
        if line is None or line == "":
            return 0
        index = 0
        count = 0
        while index < len(line):
            index = line.find(substr, index) + 1
            if index == 0:
                break
            count += 1
        return count

def isP(line):
        return isEndOfP(line) and isStrD(line)

def formated(content):
        lines = content.split("\n")
        res = ""
        for line in lines:
            endLine = ""
            if isP(line.strip()):
                endLine = "\n"
            res += line.strip() + endLine
        return res
