def wl(a):
    c = []
    b = a.split()
    i = 0
    for slowo in b:
        b[i] = slowo.capitalize()
        i += 1
    return " ".join(b)

print(wl("okno na gisz"))