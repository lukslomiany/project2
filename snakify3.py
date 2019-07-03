def pow(a, n):
    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a
print(pow(3, 5))