# -*- coding: utf-8 -*-

class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

class Person2(object):
    count = 0

    # 定义类方法
    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person2.count = Person2.count + 1

print Person2.how_many()
pp1 = Person2('Bob')
print Person2.how_many()