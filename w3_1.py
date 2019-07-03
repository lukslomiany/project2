def zlicz(n):
    a = {}
    for znak in n:
        if znak not in a:
            a[znak] = 1
        else:
            a[znak] += 1
    return a
print(zlicz("www.google.com"))