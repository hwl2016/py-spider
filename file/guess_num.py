# encoding=utf-8
import random

# 猜数字游戏
def guess_num():
    rand = random.randint(1,100)

    while True:
        print 'Enter num:'
        try:
            num = int(raw_input())
        except ValueError, e:
            print 'Please enter number!'
            continue
        if num > rand:
            print 'greater'
        elif num < rand:
            print 'lesser'
        else:
            print 'success'
            break

if __name__ == '__main__':
    guess_num()