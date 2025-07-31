k = 5
n = 30
F = [0, 1, 1]
for i in range(3, n+1):
    F.append(F[i-1] + (k*F[i-2]))
print(F[n])
