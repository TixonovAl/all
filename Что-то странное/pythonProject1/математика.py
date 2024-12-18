a1 = -3
a2 = 0
d = a2 - a1
s = a1 + a2
n = 2
while s <= 2022:
    a1, a2 = a2, a2+d
    s += a2
    n += 1
    print(a1, a2)
print(n)
