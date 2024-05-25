import math

N, L, D = input().split(" ")

N = int(N)
L = int(L)
D = int(D)

coffeMin = (N * D)

if coffeMin <= (L * 1000):
    print(L)
else:
    coffeNeed = math.ceil(coffeMin / (L * 1000))
    print(coffeNeed * L)

