# -*- coding: utf-8 -*-

import math
import time
import functools

# 装饰器
def f1(x):
    return x * x

def new_f(f):   # 装饰器函数
    def fn(x):
        print 'call ' + f.__name__ + '()'
        return f(x)
    return fn

print f1(2)
print new_f(f1)(2)  # 装饰器函数调用

# 装饰器函数调用  @ 有点像java的注解
@new_f
def f2(x):
    return x + 3

print f2(5)


def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn


@log
def add(x, y, z=5):
    return x + y + z
print add(1, 2, 3)


def performance(f):
    def fn(*args, **kw):
        t1 = int(round(time.time() * 1000))
        res = f(*args, **kw)
        t2 = int(round(time.time() * 1000))
        print 'call %s() in %sms' % (f.__name__, (t2 - t1))
        return res
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)


# 带参数的装饰器函数
def log4(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log4('DEBUG')
def test():
    pass

print test()

def performance(unit):
    def dec_performance(f):
        @functools.wraps(f) # 把原函数的所有必要属性都一个一个复制到新函数
        def wrapper(*arg, **kw):
            t = lambda : int(round(time.time() * 1000)) if unit == 'ms' else int(round(time.time()))
            t1 = t()
            res = f(*arg, **kw)
            t2 = t()
            print 'call %s() in %s %s' % (f.__name__, (t2 - t1), unit)
            return res
        return wrapper
    return dec_performance

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

print test.__name__   #  wrapper
print factorial.__name__   #  factorial




