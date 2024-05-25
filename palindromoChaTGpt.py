N = int(input())
lista = list(map(int, input().split()))

i = 0
j = len(lista) - 1
contracoes = 0

while i < j:
    if lista[i] == lista[j]:
        i += 1
        j -= 1
    elif lista[i] < lista[j]:
        lista[i + 1] += lista[i]
        i += 1
        contracoes += 1
    else:
        lista[j - 1] += lista[j]
        j -= 1
        contracoes += 1

print(contracoes)
