a = int(input("Podaj numer który dzielić:  "))
c = []
for b in range(1, a + 1):
    if a % b == 0:
        c.append(b)
print(c)