n = int(input())

registros = []
instante = 0

def get_index(registros, valor):
    for i, registro in enumerate(registros):
        if registro["valor"] == valor:
            return i
    return -1

for _ in range(n):
    evento  = input().split(" ")
    valor = int(evento[1])
    comando = evento[0]

    pos = get_index(registros, valor)

    if comando == 'R':
        if pos == -1:
            registros.append({"valor": valor,"instante": instante,"respondido": False, "tempo_acumu": 0})
        else:
            registros[pos]["instante"] = instante
            registros[pos]["respondido"] = False
    elif comando == 'E':
        if pos != -1:
            registros[pos]["tempo_acumu"] += instante - registros[pos]["instante"]
            registros[pos]["respondido"] = True
    elif comando == 'T':
       instante -= 1
       instante += valor
       continue
    instante += 1

registros.sort(key=lambda x: x["valor"])

for i in registros:
    if i["respondido"]:
        print(f"{i['valor']} {i['tempo_acumu']}")
    else:
        print(f"{i['valor']} {-1}")
