L = ['Adam', 'Lisa', 'Bart']
for item in L:
    print item

L = (1, 2, ['a', 'b', 'c'])
for item in L:
    print item

N = 10
x = 0
while x < N:
    print x
    x = x + 1

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum

L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print sum / n

for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y