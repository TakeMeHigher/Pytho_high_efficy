from collections import namedtuple
Student = namedtuple('Stu', ['name', 'age', 'sex', 'address'])
s = Student('ctz', '21', 'male', '云南昆明')
print(s)
print(s.address)
print(isinstance(s, tuple))