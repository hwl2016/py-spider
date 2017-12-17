# -*- coding: utf-8 -*-
import re

class Person(object):

    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count += 1

print Person.how_many()

p1 = Person('Bob')

print Person.how_many()

def flt(str):
    if not re.match(r'^_', str):
        return str

# 获取对象信息
print type(123)
print dir(123)
print dir(p1)
# 过滤私有属性
print filter(lambda ele: ele if not re.match(r'^_', ele) else '', dir(p1))
# print filter(flt, dir(p1))

class Person2(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            # self.k = v    # 这种方法不行
            setattr(self, k, v)

p2 = Person2('Bob', 'Male', age=18, course='Python')
print p2.age
print p2.course
