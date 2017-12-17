# -*- coding: utf-8 -*-

class Person(object):
    addr = 'Earth'  # 直接定义类属性
    def __init__(self, name, gender, birth, job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__job = job    # 双下划线定义的私有属性 不能被外部访问

    def get_job(self):
        return self.__job

p1 = Person('Mark', 'Male', '1990-12-12', 'teacher')
p2 = Person('Lily', 'Female', '1992-02-09', 'student')

print p1.name
print p2.gender
# print p2.__job    # 访问不到私有属性 会报错的
print 'p2 job:', p2.get_job()
print p1 == p2
print 'Person addr:', Person.addr
Person.addr = 'China'
print 'Person addr:', Person.addr
print 'p1 addr:', p1.addr
