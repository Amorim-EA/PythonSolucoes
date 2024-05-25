N = int(input())

numeros = []

for _ in range(N):
    fala = int(input())
    if fala == 0:
        if numeros:
            numeros.pop()
    else:
        numeros.append(fala) 

print(sum(numeros))

