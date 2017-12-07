# -*- coding: utf-8 -*-

def readFile():
    fileName = 'haha.txt'
    file = open(fileName, 'r+')
    try:
        content = file.read()
        # content = file.readline()
        # content = file.readlines()
        print content
    finally:
        file.close()

def iterReadFile():
    fileName = 'haha.txt'
    file = open(fileName, 'r+')
    try:
        # 使用迭代器在不消耗大量内存的情况下 完成对文件的全部读取
        iter_f = iter(file)
        lines = 0
        for line in iter_f:
            lines += 1
        print lines
    finally:
        file.close()

def writeFile():
    fileName = 'haha2.txt'
    file = open(fileName, 'w+')
    try:
        file.write('123...')
    finally:
        file.close()

if __name__ == '__main__':
    writeFile()