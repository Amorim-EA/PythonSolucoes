amigos = [int(input()) for _ in range(4)]
amigos.sort()

dupla1 = amigos[0] + amigos[3]
dupla2 = amigos[1] + amigos[2]

print(abs(dupla1 - dupla2)) 
