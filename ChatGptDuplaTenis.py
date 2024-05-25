# Leitura dos níveis dos jogadores
A, B, C, D = [int(input()) for _ in range(4)]

# Possíveis combinações de duplas
combinacoes = [
    (A + B, C + D),
    (A + C, B + D),
    (A + D, B + C)
]

# Inicializa a menor diferença com um valor grande
menor_diferenca = float('inf')

# Calcula a menor diferença entre os níveis dos times
for dupla1, dupla2 in combinacoes:
    diferenca = abs(dupla1 - dupla2)
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca

# Imprime a menor diferença encontrada
print(menor_diferenca)

