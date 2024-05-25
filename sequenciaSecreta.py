N = int(input());

V = [];

for i in range(N):
        V.append(int(input()));

res = 0
ultim = 0

for i in V:
    if ultim != i:
         res += 1
    ultim = i


print(res)
