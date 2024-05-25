n = int(input())

vetor = [(int(i)) for i in input().split(" ")]

normal = sum(range(1, n+1))
quanti_blocos = sum(i for i in vetor)

quanti_prime_bloco = (quanti_blocos - normal) // n + 1

moves = 0

for i in vetor:
    if i > quanti_prime_bloco:
        moves += i - quanti_prime_bloco
    quanti_prime_bloco += 1

if ((quanti_blocos - normal) %  n) != 0:
    moves = -1

print(moves)
