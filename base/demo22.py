# -*- coding: utf-8 -*-

# 特殊方法
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)

    __repr__ = __str__

    def __cmp__(self, other):
        if self.score > other.score:
            return -1
        elif self.score < other.score:
            return 1
        else:
            if self.name < other.name:
                return -1
            elif self.name > other.name:
                return 1
            else:
                return 0

p = Person('Huwl', 'male')
s = Student('Bob', 'male', 95)
s2 = Student('Mark', 'male', 60)
s3 = Student('Lily', 'female', 95)

print p
print s
print sorted([s, s2, s3])

class Fib(object):

    def __init__(self, num):
        if num == 1:
            self.nums = [0]
        elif num == 2:
            self.nums = [0, 1]
        else:
            L = [0, 1]
            i = 2
            while (i < num):
                L.append(L[i - 2] + L[i - 1])
                i += 1
            self.nums = L

    def __str__(self):
        return str(self.nums)

    def __len__(self):
        return len(self.nums)

f = Fib(10)
print f
print len(f)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __int__(self):  # 将有理数转成int类型
        return self.p // self.q

    def __float__(self):  # 将有理数转成float类型
        return float(self.p) / self.q

    def __str__(self):
        c = gcd(self.p, self.q) # 化简时求最大公约数
        return '%s/%s' % (self.p / c, self.q / c)

    __repr__ = __str__

# 求a，b的最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

print int(Rational(7, 2))
print float(Rational(7, 2))
print int(Rational(1, 3))
print float(Rational(1, 3))