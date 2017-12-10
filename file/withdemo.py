# encoding=utf-8

import os

try:
    f = open('1.txt')
    print 'in try f.read():', f.read()
    f.seek(-5, os.SEEK_SET)
except IOError, e:
    print 'catch IOError:', e
except ValueError, e:
    print 'catch ValueError:', e
finally:
    try:
        f.close()
    except Exception, e:
        print 'catch Error:',e
print 'try-finally:', f.closed

try:
    with open('1.txt') as f1:
        print 'in with f1.read():', f1.read()
        f1.seek(-5, os.SEEK_SET)
except IOError, e:
    print 'catch with IOError:', e
    print 'with:', f1.closed


