# 取出列表中的非负数
import random
l = [random.randint(-10, 10) for _ in range(10)]
print(l)
# 方法一 low
# res = []
# for i in l:
#     if i > 0:
#         res.append(i)
# print(res)

#方法二
# res = filter(lambda x: x >= 0, l)
# print(list(res))

# 方法三

res = [i for i in l if i >= 0]
print(res)