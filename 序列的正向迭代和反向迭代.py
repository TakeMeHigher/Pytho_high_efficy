# 首先有内置方法可以实现
l = [1, 2, 3, 4, 5]
# 正向迭代
l_z = iter(l)
for u in l_z:
    print(u)

# 反向迭代

l_f = reversed(l)
for i in l_f:
    print(i)


# 其中 l_z 和 l_f 都是一个迭代器


# 下面我们自己写代码来实现这两个方法
class IterRes(object):
    def __init__(self, start, end, step=0.5):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for i in reversed(IterRes(1, 5)):
    print(i)
