"""
If you just assign a object(list,dict or object) to a variable only the referece gets assigned(ie shallow copy).
If u want to do a deepcopy then use deepcopy form copy

"""
from copy import deepcopy
items = dict(name='manju')
temp = items
temp1 = items
print(id(temp))
print(id(temp1))
print(id(items))

dtemp = deepcopy(items)
print(id(dtemp))