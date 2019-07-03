from random import randint
a = [randint(0,20) for _ in range (10, 20)]
print(a)
def usunduplik(lista):
    b = []
    for x in lista:
        if x not in b:
            b.append(x)
    return b

def usunduplik2(lista):
    c = set(a)
    return c

print(usunduplik(a))
print(usunduplik2(a))
