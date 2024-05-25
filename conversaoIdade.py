age = int(input());

Y = (age//365);
M = ((age%365)//30);
D = ((age%365)%30);

print(f"{Y} anos(s)\n{M} mes(es)\n{D} dia(s)");

