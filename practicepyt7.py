a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for x in a:
    if x % 2 == 0 and x != 0:
        b.append(x)
print(b)
c = [x for x in a if x % 2 == 0 and x != 0]
print(c)
if len(b) > 2:
    print("dlugość b większa od dwóch cwiczenie gita")
print("vgvhgchc")