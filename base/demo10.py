# -*- coding: utf-8 -*-

# 切片
L = range(1, 101)

print L

print L[:]

# 前10个数
print L[:10]

# 3的倍数
print L[2::3]

# 不大于50的5的倍数
print L[4:50:5]

# 最后10个数
print L[-10:]

# 最后10个5的倍数
print L[4::5][-10:]

# 字符串切片
str = 'ABCDEFG'

print str[:3]
print str[-3:]
print str[::2]

def firstCharUpper(s):
    a = s[:1].upper()
    b = s[1:]
    return a + b

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

