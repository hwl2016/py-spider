# encoding=utf-8

# magic method: 类的属性控制  __setattr__(self, name, value)  __getattr__(self, name)  __getattribute__(self, name)  __delattr__(self, name)
# __getattr__(self, name): 查询的属性不存在时调用
# __getattribute__(self, name): 每次查询的属性都调用

class Programer(object):

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __getattribute__(self, item):
        print 'call __getattribute__ method'
        # return getattr(self, item)    # 注意不能这么写 否则会无限递归  RuntimeError: maximum recursion depth exceeded
        # return self.__dict__[item]  # 注意不能这么写 否则会无限递归  RuntimeError: maximum recursion depth exceeded
        return super(Programer, self).__getattribute__(item)

    def __setattr__(self, key, value):
        print 'call __setattr__ method'
        # setattr(self, key, value)     # 注意不能这么写 否则会无限递归  RuntimeError: maximum recursion depth exceeded
        self.__dict__[key] = value

if __name__ == '__main__':
    p = Programer('Albert', 25)
    print p.name
