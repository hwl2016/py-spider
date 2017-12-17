# -*- coding:utf-8 -*-
classmates = ['Michael', 100, True]
print classmates

L = ['Adam', 'Lisa', 'Bart']

print L[0] # Adam
print L[-1] # Bart

# 向数组末尾添加一个元素  append方法
L.append('Paul')
# 向数组首位添加一个元素  insert
L.insert(0, 'Michael')

# 删除元素
removeClassmate = L.pop()   # 删除最后一个元素 并返回这个被删除的元素
removeClassmate2 = L.pop(1)   # 删除第二个元素 并返回这个被删除的元素

print L
print removeClassmate
print removeClassmate2

# 替换数组的元素  对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。
L[0] = 'Mark'
print L


# tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
t = ('Adam', 'Lisa', 'Bart')
print t[1]
print t[-1]

# 创建单个元组  单元素 tuple 要多加一个逗号“,”
tt = ('aaa',)
print tt

# 可变的tuple
ttt = ('a', 'b', ['A', 'B'])
li = ttt[2]
li[0] = 'X'
li[1] = 'Y'
li.append('Z')

print ttt