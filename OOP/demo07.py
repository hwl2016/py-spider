# encoding=utf-8

# magic method: 类与运算符  __add__  __class__  __contains__  __delattr__  __doc__  __eq__
# 比较运算符： __cmp__(self, other)  __eq__(self, other)  __lt__(self, other)  __gt__(self, other)
# 数字运算符： __add__(self, other)  __sub__(self, other)  __mul__(self, other)  __div__(self, other)
# 逻辑运算符： __or__(self, other)  __and__(self, other)

class Programer(object):

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programer):
            if other.age == self.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return other.age + self.age
        else:
            raise Exception('The type of object must be Programer')

if __name__ == '__main__':
    p1 = Programer('Albert', 25)
    p2 = Programer('Bill', 30)
    print p1 == p2
    print p1 + p2
