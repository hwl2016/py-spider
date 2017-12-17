# -*- coding: utf-8 -*-

L = range(1, 101)
for i in L:
    if i % 7 == 0:
        print i

# 索引迭代
L = ['Adam', 'Lisa', 'Bart', 'Paul']
enu = enumerate(L)
for index, name in enu:
    print index, '-', name

print enu

for t in enumerate(L):
    print t, '=>', t[0], ':', t[1]

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for score in d.itervalues():
    sum += score
print '平均分：', sum / 4
print d
print d.itervalues()    # <dictionary-valueiterator object at 0x02C288A0>
print d.values()

print '==================';

# 迭代key和value
for key in d:
    print key, ':', d[key]

print '=================='

for key, value in d.iteritems():
    print key, ':', value

print '=================='

print d.items()
print d.iteritems() #<dictionary-itemiterator object at 0x02CA88A0>