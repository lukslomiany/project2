def dystans(*args):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return d

x1 = int(input("Podaj x 1 pkt"))
y1 = int(input("Podaj y 1 pkt"))
x2 = int(input("Podaj x 2 pkt"))
y2 = int(input("Podaj y 2 pkt"))
print(dystans(x1, y1, x2, y2))