from random import randint

m = randint(1, 13)
n = randint(1, 15)
a = []
b = []
e = []
print(m)
print(n)
for x in range(m):
    i = randint(0, 20)
    a.append(i)
print(a)
for y in range(n):
    j =  randint(0, 20)
    b.append(j)
print(b)
print()
for o in a:
    if o in b:
        if o not in e:
            e.append(o)
print(e)

