#-*- encoding=utf-8 -*-

import sys
import os

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

APP_NAME = "TextSplitOutput"
APP_AUTHOR = "allen wong"
APP_VERSION = "0.5 build(161008)"
APP_LICENSE = "GPL"

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

LIST_FLAG_QUICK = ["q@", "quick", "out-quick.txt"]
LIST_FLAG_LOW = ["l@", "low", "out-low.txt"]
LIST_FLAG_HIGH = ["h@", "high", "out-high.txt"]

FILE_NAME_PROCESS = "out-process.txt"

FLAG_NO_PROCESS = "#"

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

# check string 是否 bad, 如果 msg != "" 则会显示, exit 如为 True 则在 check bad 是 exit script
# bool type: debug, exit
def checkStringBad(str, msg):
    if not str:
        if msg != "":
            print("string is empty, " + msg)
        return False
    if len(str) < 1:
        if msg != "":
            print("string is empty, " + msg)
        return False
    return True

# file 要为 utf-8 格式
# return:
#   '' = fail
#   list = ok
def readFromFile(fn):
    if not os.path.isfile(fn):
        print('request file not exists:', fn)
        return ''
    # read file
    ff = open(fn, 'r')
    lines = ff.readlines()
    ff.close()
    return lines
    #f = codecs.open(fn,'r',encoding='utf8')
    #lines = f.readlines()
    #return lines

# return:
#   "" = fail
#   string flag = OK
def findLineStrFlag(lineStr):
    if not checkStringBad(lineStr, ""):
        return ""
    lineFlag = ""
    if lineStr.find( LIST_FLAG_QUICK[0] ) == 0:
        print("find QUICK: " + lineStr)
        lineFlag = LIST_FLAG_QUICK[0]
    elif lineStr.find( LIST_FLAG_LOW[0] ) == 0:
        print("find LOW: " + lineStr)
        lineFlag = LIST_FLAG_LOW[0]
    elif lineStr.find( LIST_FLAG_HIGH[0] ) == 0:
        print("find HIGH: " + lineStr)
        lineFlag = LIST_FLAG_HIGH[0]
    elif lineStr.find( FLAG_NO_PROCESS ) == 0:
        print("find no process: " + lineStr)
        lineFlag = FLAG_NO_PROCESS
    return lineFlag

def getFileNameFromFlag(flag):
    fn = ""
    if flag == LIST_FLAG_QUICK[0]:
        fn = LIST_FLAG_QUICK[2]
    elif flag == LIST_FLAG_LOW[0]:
        fn = LIST_FLAG_LOW[2]
    elif flag == LIST_FLAG_HIGH[0]:
        fn = LIST_FLAG_HIGH[2]
    else:
        print("unknow flag to write file: " + flag)
        exit(1)
    return fn

def storeToFlagFile(flag, lineStr):
    fn = getFileNameFromFlag(flag)
    if fn == "":
        return
    if not checkStringBad(lineStr, ""):
        return
    lineStr = lineStr[2:]        # 截取 2-N
    lineStr = lineStr.strip()    # 去掉前后空格
    appendToFile(fn, lineStr)
    print("  ---> success write: " + lineStr)

def appendToFile(fn, lineStr):
    ff = open(fn, 'a')      # append to file, 如 file 不存在, 则 create
    ff.write(lineStr + "\n")
    ff.close()

# 在传入字串尾, 加上 空白符, 使其长度达到指定长度
def widthString(str, length):
    s = ""
    if checkStringBad(str, ""):
        s = str
    if length < 1:
        length = 1
    elif length > 99:
        length = 99
    if len(s) >= length:
        return s
    for i in range(length-len(s)):
        s += " "
    return s

def processSplit(lineStr):
    if not checkStringBad(lineStr, ""):
        return ""
    lineStr = lineStr.strip()    # 去掉前后空字符
    lineFlag = findLineStrFlag(lineStr)
    if lineFlag == "":
        print("unknow FLAG: " + lineStr)
        return ""
    elif lineFlag == FLAG_NO_PROCESS:
        return ""
    storeToFlagFile(lineFlag, lineStr)
    return lineFlag

def processDiff(index, flag, lineStr):
    space = widthString(flag, 10)
    lineNum = widthString(str(index+1), 3)
    s = "[ %s ] %s %s" % (space, lineNum, lineStr)
    appendToFile(FILE_NAME_PROCESS, s)

def printAppInfo():
    print("app name: " + APP_NAME)
    print("author: " + APP_AUTHOR)
    print("version: " + APP_VERSION)
    print("license: " + APP_LICENSE)
    print("")

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
def main():
    printAppInfo()
    if len(sys.argv) < 2:
        print("request arg 1 is input file name.")
        print("can use 'test-input.txt'")
        return
    fn = sys.argv[1]
    lines = readFromFile(fn)
    if lines == '':
        return False
    if not lines:
        return False
    for index, lineStr in enumerate(lines):
        newLineStr = lineStr
        # 去掉换行符, 否则 string 还会算有一个 character
        newLineStr = newLineStr.replace("\r\n", "")
        newLineStr = newLineStr.replace("\n", "")
        flag = processSplit(newLineStr)
        processDiff(index, flag, newLineStr)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
main()

