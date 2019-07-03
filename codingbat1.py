import random
a = []
m = random.randint(3, 8)
print(m)
for x in range(m):
    a.append(random.randint(0, 20))
print(a)
# różnica między największym a najmniejszym wyrazem
min = a[0]
max = a[0]
i = 1
while i < (len(a)):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
    i += 1
print(f" Różnica miedzy max i min wynosi: {max - min}")
#
# suma ciągu gdy ai < 13
#
# k = 0
# i = 0
# while i < (len(a)-1):
#     if a[i] < 13:
#         k += a[i]
#     i += 1
# print(k)
#
#przesuwanie ciągu w lewo
# k = int(input("Podaj ile razy przesunąć ciąg:  "))
# l = 0
# while l < k:
#     c = a[0]
#     for i in range(len(a)-1):
#         a[i] = a[i + 1]
#     a[-1] = c
#     l += 1
# print(a)
