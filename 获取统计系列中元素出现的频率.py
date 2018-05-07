# 1.统计随机列表中出现频率最多的三个数
from random import randint
from collections import Counter

l = [randint(1, 10) for i in range(30)]
c = Counter(l)
c_l = c.most_common(3)
print(c_l)

