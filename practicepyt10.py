import random
from random import randint

m = randint(1, 13)
n = randint(1, 15)
a = []
b = []
e = []
f = random.sample(range(5), 3)
print(m)
print(n)
print(f"f: {f}")
for x in range(m):
    a.append(randint(0, 20))
print(a)
for y in range(n):
    b.append(randint(0, 20))
print(b)
print()
# for o in a:
#     if o in b:
#         if o not in e:
#             e.append(o)
e = [o for o in a if o in a if o in b if o not in e]
print(e)