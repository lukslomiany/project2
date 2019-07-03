from random import randint
a = randint(1, 10)
i = 0
while True:
    b = input("Podaj liczbę od 1 do 9 lub k")
    if b == "k":
        print("koniec")
        break
    if b != "k":
        i += 1
        if int(b) == a:
            print("dobrze")
            break
        elif int(b) > a:
            print("za duzo")
            continue
        elif int(b) < a:
            print("za malo")
            continue
if i > 0:
    print(f"użytkownik zgadywał {i} razy")
