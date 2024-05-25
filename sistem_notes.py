quanti_alunos = int(input())

fichaAluno = [{"nome": str(input()), "notas": [float(i) for i in input().split(" ")], "media": 0} for _ in range(quanti_alunos)]

i = 0
for aluno in fichaAluno:
    notas = aluno["notas"]
    if len(notas) == 1:
        fichaAluno[i]["media"] = (notas[0] + 0) / 2
    elif len(notas) == 2:
        fichaAluno[i]["media"] = sum(notas) / 2
    elif len(notas) == 3:
        fichaAluno[i]["media"] = sum(notas) / 3
    else:
        fichaAluno[i]["media"] = sum(sorted(notas, reverse=True)[:3])/3
    i += 1

[print(f"{aluno['nome']}: {aluno['media']:.1f}")  for aluno in fichaAluno]
