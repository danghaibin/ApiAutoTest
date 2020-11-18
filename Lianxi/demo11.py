import random
from random import shuffle
print(random.random())

print(random.randint(1,10))
# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
print([j for i in a for j in i])


a = [1,3,65,98,43]
sorted(a)
print(a)


names = ['zhangsan','lisi','wamgeu','fsdfs']
shuffle(names)
print(names)

a = random.choice(names)
print(a)