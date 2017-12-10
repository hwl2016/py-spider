# encoding=utf-8

class Mycontext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print '__enter__'
        return self

    def do_self(self):
        a = 'aaa'
        print 'do_self'
        print int(a)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'
        print 'Error:', exc_type, 'info:', exc_val

if __name__ == '__main__':
    with Mycontext('huwl') as c:
        print c.name
        c.do_self()