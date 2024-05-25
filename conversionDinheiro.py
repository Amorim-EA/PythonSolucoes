list = [100, 50, 20, 5, 2, 1];

numb = float(input());

for i in list:
    qtdNotas = numb // i;
    numb = numb - (qtdNotas * i);
    print(f"{qtdNotas} notas de R${i}");

