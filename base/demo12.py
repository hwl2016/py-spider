# -*- coding: utf-8 -*-

# 生成列表

L = range(1,11)

print L

# 列表生成式

LL = [x * x for x in range(1, 11)]

print LL

print [x * (x + 1) for x in range(1, 100, 2)]

print '========================'

# 复杂表达式
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    # % 用来格式化数据的
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

print '========================'

# 条件过滤
print [x * x for x in range(1, 11) if x % 2 == 0]

print '========================'

# 把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]

print toUppers(['Hello', 'world', 101])

# 多层表达式  双层循环
print '========================'
print [m + n for m in 'ABC' for n in '123']

# 找对称的三位数 如121
print '========================'
print [x * 100 + y * 10 + z for x in range(1, 10) for y in range(0, 10) for z in range(1, 10) if x == z]

