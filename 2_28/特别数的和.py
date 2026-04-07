s = int(input())

sum = 0
for i in range(1,s+1):
    for j in str(i):
        if j in '2'or j in '0'or j in '1'or  j in '9':
            sum += i
            break
print(sum)
