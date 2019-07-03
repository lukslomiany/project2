t = input("Podaj słowo")
n = int(input("Podj ktora litere usunąc"))
if n < len(t):
    print(f"{t[:n]}{t[n+1:]}")
else:
    print("za duze n")