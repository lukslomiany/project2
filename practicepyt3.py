a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = len(a)
i = 0
d = []
j = 0

for i in range(b):
    if a[i] < 5:
        c = a[i]
        print(c, end = "  ")
print()
e = int(input("Od jakie mniejsze od"))
for j in range(b):
    if a[j] < e:
        c = a[j]
        d.append(c)
print(d)