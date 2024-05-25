N = int(input())

lista = [int(elem) for elem in input().split(" ")]


i = 0
j = len(lista) - 1
contracoes = 0

while i < j:
    elem_i = lista[i]
    elem_j = lista[j]

    if elem_i == elem_j:
        i += 1
        j -= 1
    elif elem_i > elem_j:
        soma = lista[j] + lista[j-1]
        lista.pop(j)
        lista.pop(j-1) 
        lista.insert(j-1, soma)
        j -= 1
        contracoes += 1
    else:
        soma = lista[i] + lista[i+1]
        lista.pop(i)
        lista.pop(i)
        lista.insert(i, soma)
        j -= 1
        contracoes += 1

print(contracoes)
