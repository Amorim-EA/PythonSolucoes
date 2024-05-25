S = int(input())
A = int(input())
B = int(input())


min_max = [0, 0]

for i in range(A, B+1):
    algs = [int(j) for j in str(i)]
    if sum(algs) == S:
        if min_max[0] == 0:
            min_max[0] = i
        else:
            min_max[1] = i
        if min_max[1] == 0:
            min_max[1] = i

print(f"{min_max[0]}\n{min_max[1]}")
