# 字典找出value大于90的
from random import randint
dic = {i: randint(60,100) for i in range(20) }
# 传统方法忽略
we_d = {k: v for k, v in dic.items() if v > 90}
print(we_d)


# 集合 找出能被3整处的
s = {i for i in range(1,30)}
we_s = {i for i in s if i % 3 == 0}
print(we_s)