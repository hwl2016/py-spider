# encoding=utf-8

class AAA:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        print 'call...'
        self.b = b

    def __str__(self):
        return "(AAA: %d, %d)" % (self.a, self.b)

if __name__ == '__main__':
    t = AAA(123)
    t(456)  # 调用t时才调用 __call__ 方法
    print t # 调用 __str__ 方法
