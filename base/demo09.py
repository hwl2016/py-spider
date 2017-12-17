# -*- coding: utf-8 -*-

import math

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print x, y
print move(100, 100, 60, math.pi / 6)   # 返回一个tuple

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(100)

# 可变参数
def fn(*args):
    print args

fn(1,2,'a')
