def na_odwrot(a):
    b = a.split()
    c = b[::-1]
    d = " ".join(c)
    print(d)

print(na_odwrot("Ala ma kota"))

def licz(a):
    return a.count("a")
print(licz("Ala ma kota"))