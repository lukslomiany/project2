from random import randint
a = ['kamien', 'papier', 'nozyce']

while True:
    i = randint(0, 2)
    x = input("kamien, papier, nozyce:   ")
    print(f"komp wybrał:  {a[i]}")
    if x == 'kamien' and a[i] == 'papier':
        print("przegrałeś")
        continue
    elif x == 'papier' and a[i] == 'nozyce':
        print("przegrales")
        continue
    elif x == 'nozyce' and a[i] == 'kamien':
        print("przegrales")
        continue
    elif x == a[i]:
        print("remis")
        continue
    else:
        print("wygrales")
    break
