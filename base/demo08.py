# -*- coding: utf-8 -*-

# 字典 类似于js的对象字面量
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

print d

l = len(d)

print 'dict d length:', l

if('Adam' in d):
    print 'Adam\'s score:', d['Adam']

print 'Bart\'s score:', d.get('Bart')
print 'Paul\'s score:', d.get('Paul')

# 遍历dict
for key in d:
    print key + '\'s score:', d[key]

d['Paul'] = 72  # 新增
d['Bart'] = 72  # 更新
print d


# set   不重复
s = set(['A', 'B', 'C', 'C'])
print s # set(['A', 'C', 'B'])
print len(s)    # 3
print 'A' in s
print 'b' in s

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'THU'
if x in weekdays:
    print 'ok'
else:
    print 'ng'

# 遍历set
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for item in s:
    print item

# add
s.add('haha')

# remove
if ('Bart', 59) in s:
    s.remove(('Bart', 59))

print s