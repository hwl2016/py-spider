# -*- coding: utf-8 -*-

# 类的继承
class Person(object):
    __count = 0
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Person.__count += 1

    @classmethod
    def get_cnt(cls):
        return cls.__count

# 继承Person类
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender) # 初始化父类
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender) # 初始化父类
        self.course = course

s1 = Student('Mark', 'male', 90)
print s1
print s1.name
print s1.gender
print s1.score
print s1.get_cnt()

t1 = Teacher('Smith', 'male', 'Chinese')
print t1
print t1.name
print t1.gender
print t1.course
print t1.get_cnt()

print isinstance(t1, Person)    # True
print isinstance(t1, Student)    # False
print isinstance(t1, Teacher)    # True
print isinstance(t1, object)    # True

class Fib(object):

    def __init__(self):
        pass

    def __call__(self, num):
        a, b, L = 0, 1, []  # 类似ES6的解构赋值
        for x in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib()
print f(10)
