a = input("Podaj wyraz:  ")
b = []
c = []
f = a[::-1]
g = a[::1]
for x in a:
    b.append(x)
for y in a:
    c.insert(0, y)
print(a)
print(b)
print(c)
print(f)
print(g)
if a == f:
    print("polindrome")
else:
    pass
if b == c:
    print(" czyta sie tak samo do przodu jak do tyłu")
else:
    print("koniec")