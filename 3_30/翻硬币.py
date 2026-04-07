start = list(str(input()))
end = list(str(input()))

count = 0 # 统计次数

for i in range(len(start)-1):
    if start[i] != end[i]:
        if start[i] == '*':
            start[i] = 'o'
        else:
            start[i] = '*'
        if start[i+1] == '*':
            start[i+1] = 'o'
        else:
            start[i+1] = '*'
        count += 1
print(count)