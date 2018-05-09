from random import randint
d = {i: randint(1, 20)for i in 'abcxy'}
print(d)
# 1
a = list(zip(d.values(), d.keys()))
print(a)
s= sorted(a)
print(s)

# 2
li = d.items()
ss = sorted(li, key=lambda x: x[1])
print(ss)