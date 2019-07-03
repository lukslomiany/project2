a = int(input("podaj licznik"))
b = int(input("Pdaj mianownik"))
if b == 0:
    print("Nie dzielimy przez 0")
elif a % b == 0:
    print("licznik jest podzielny przez mianownik")
if a % 4 == 0:
    print("licznik jest podzielny przez 4")
if a % 2 == 0:
    print("parzysta")
else:
    print("nieparzysta")