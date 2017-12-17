# encoding=utf-8

# magic method: 类的展现  __str__  __repr__   __unicode__    __dir__

class Programer(object):

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

if __name__ == '__main__':
    p = Programer('Albert', 25)
    print p
    print dir(p)
