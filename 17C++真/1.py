import itertools

n = 13
m = (n+1)//2
jc = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        jc[i][j] += i*j*(i+j)
        if i == j:
            jc[i][j] = jc[i][j] * 2
        if i == 1 or i == n or j == 1 or j == n:
            jc[i][j] = jc[i][j] / 2
if n % 2 != 0:
    jc[m][m] = jc[m][m] +100
for i, j in itertools.product(range(1, n+1), range(1, n+1)):
    print(int(jc[i][j]), end=" ")
total = sum(jc[i][j] for i in range(1, n+1) for j in range(1, n+1))
print(total)

