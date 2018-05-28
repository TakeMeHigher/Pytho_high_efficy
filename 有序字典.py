from collections import OrderedDict
# OrderedDict 他会按元素加入字典的顺序排序

dic = OrderedDict()
dic['d'] = 5
dic['a'] = 2
dic['e'] = 1
dic['c'] = 3
dic['b'] = 6

for k in dic:
    print(k)
print('----------------------------------')
aa = {}
aa['d'] = 5
aa['a'] = 2
aa['e'] = 1
aa['c'] = 3
aa['b'] = 6
for k in aa:
    print(k)