# encoding:utf-8
from random import randint, sample
d1 = {k: randint(1, 10) for k in sample('abcdef', 3)}
d2 = {k: randint(1, 10) for k in sample('abcdef', 4)}
d3 = {k: randint(1, 10) for k in sample('abcdef', 5)}

# low
res = []
for i in d1:
    if i in d2 and i in d3:
         res.append(i)
print(res)

# 对于Python2
print(d1.viewkeys() & d2.viewkeys() & d3.viewkeys())

# Python2 有用
# 对于n轮来说 用下面这个
ss = map(dict.viewkeys, [d1, d1, d3])
print (ss)
aa = reduce(lambda a, b: a & b, ss)
print aa
