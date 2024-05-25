N = int(input())
O = []

for i in range(N):
    O.append(input())

for i in O:
    A = i.split(" ")

    tempo = A[1]
    minutos = int(A[0])

    if tempo == "1T" and minutos <= 45:
        print(minutos)
    elif tempo == "1T" and minutos >= 45:
        print(f"45+{minutos % 45}")
    elif tempo == "2T" and minutos <= 45:
        print(45 + minutos)
    else:
        print(f"90+{minutos % 45}")

