import re
from collections import Counter

with open('friend', 'r') as f:
    data = f.read()
    data_l = re.split(r'\W+', data)
data_dic = Counter(data_l)
print(data_dic.most_common(10))
