# -*- coding: utf-8 -*-

import math
import functools

def haha(x, y, f):
    return f(x) + f(y)

print haha(3, 4, math.sqrt)
print haha(25, 9, math.sqrt)

L = ['adam', 'LISA', 'barT']

def format_name(str):
    a = str[:1]
    b = str[1:]
    return a.upper() + b.lower()

print map(format_name, L)

def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])

def is_sqr(x):
    if math.sqrt(x) % 2 == 0 or math.sqrt(x) % 2 ==1:
        return x

print filter(is_sqr, range(1, 101))

def cmp_ignore_case(s1, s2):
    s11 = s1.lower()
    s22 = s2.lower()
    return cmp(s11, s22)

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


# 高阶函数
def calc_prod(lst):
    def aa():
        return reduce(prod, lst)
    return aa

f = calc_prod([1, 2, 3, 4])
print f()

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(x):
            def ff():
                return x * x
            return ff
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

# 匿名函数
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))

print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', ' str ', '  ', ' END'])

myabs = lambda x: -x if x < 0 else x
print myabs(-1)
print myabs(1)

# 偏函数 当一个函数有很多参数时，调用者就需要提供多个参数。如果减少参数个数，就可以简化调用者的负担。
print int('12345', 8)   # 将 '12345' 当做8进制数 然后转成10进制数  5349
print int('12345', 16)   # 将 '12345' 当做16进制数 然后转成10进制数  74565

int2 = functools.partial(int, base=2)

print int2('1000000000000')

sorted_ignore_case = functools.partial(sorted, key=str.lower)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

