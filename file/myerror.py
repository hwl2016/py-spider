# encoding=utf-8

# 自定义异常

class FileError(IOError):
    pass

class CustomError(Exception):
    def __init__(self, info):
        Exception.__init__(self)
        self.errorinfo = info
        print id(self)  # 打印对象在内存中的地址
    def __str__(self):
        return 'CustomError:%s' % self.errorinfo

def test1():
    try:
        raise FileError, 'test FileError'
    except FileError, e:
        print e

def test2():
    try:
        raise CustomError('test CustomError')   # 自定义异常需要主动抛出
    except CustomError, e:
        print 'Error id:%d, %s' % (id(e), e)

if __name__ == '__main__':
    test2()
