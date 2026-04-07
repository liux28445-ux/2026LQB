import itertools

count = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in itertools.permutations(arr):
    A = i[0]
    B = i[1]
    C = i[2]

    DEF = i[3] * 100 + i[4] * 10 + i[5]
    GHI = i[6] * 100 + i[7] * 10 + i[8]
    if A+ B/C + DEF/GHI == 10:
        count += 1

print( count)