#-*- encoding=utf-8 -*-

import sys
import os

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
FLAG_QUICK = "q@"
FLAG_LOW = "l@"
FLAG_HIGH = "h@"

FILE_NAME_QUICK = "out-quick.txt"
FILE_NAME_LOW = "out-low.txt"
FILE_NAME_HIGH = "out-high.txt"

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
    if lineStr.find( FLAG_QUICK ) == 0:
        print("find QUICK: " + lineStr)
        lineFlag = FLAG_QUICK
    elif lineStr.find( FLAG_LOW ) == 0:
        print("find LOW: " + lineStr)
        lineFlag = FLAG_LOW
    elif lineStr.find( FLAG_HIGH ) == 0:
        print("find HIGH: " + lineStr)
        lineFlag = FLAG_HIGH
    elif lineStr.find( FLAG_NO_PROCESS ) == 0:
        print("find no process: " + lineStr)
        lineFlag = FLAG_NO_PROCESS
    return lineFlag    

def getFileNameFromFlag(flag):
    fn = ""
    if flag == FLAG_QUICK:
        fn = FILE_NAME_QUICK
    elif flag == FLAG_LOW:
        fn = FILE_NAME_LOW
    elif flag == FLAG_HIGH:
        fn = FILE_NAME_HIGH
    else:
        print("unknow flag to write file: " + flag)
        exit(1)
    return fn

def writeToFile(flag, lineStr):
    fn = getFileNameFromFlag(flag)
    if fn == "":
        return
    if not lineStr:
        print("write string is empty")
        return
    if len(lineStr) < 1:
        print("write string is empty")
        return
    lineStr = lineStr[2:]        # 截取 2-N
    lineStr = lineStr.strip()    # 去掉前后空格
    ff = open(fn, 'a')      # append to file, 如 file 不存在, 则 create
    ff.write(lineStr + "\n")
    ff.close() 
    print("  ---> success write: " + lineStr)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
def main():
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
    for index, lineStr in enumerate( lines ):
        newLineStr = lineStr
        # debug
        # print("line string len: %d" % len(newLineStr) )
        # 去掉换行符, 否则 string 还会算有一个 character
        newLineStr = newLineStr.replace("\r\n", "")
        newLineStr = newLineStr.replace("\n", "")
        if not checkStringBad(newLineStr, ""):
            continue
        newLineStr = newLineStr.strip()    # 去掉前后空字符
        lineFlag = findLineStrFlag(newLineStr)
        if lineFlag == "":
            print("unknow FLAG: " + newLineStr)  
            continue
        elif lineFlag == FLAG_NO_PROCESS:
            continue
        writeToFile(lineFlag, newLineStr)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
main()
