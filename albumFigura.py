N = int(input());
M = int(input());
X = [];

for i in range(M):
	X.append(int(input()));

X = set(X);
print(N-len(X));
