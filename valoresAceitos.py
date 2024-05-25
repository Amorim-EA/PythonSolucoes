A, B, C, D = [int(num) for num in input().split(" ")];
print("Valores aceitos" if (B > C) and (D > A) and ((C + D) > (A + B)) and ((C and D) > 0) and ((A % 2) == 0) else "Valores nao aceitos")
