import bisect
import itertools
n,k = map(int,input().split())
list1 = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1,n):
        if i < j and (j-i)%4==0:
            list1[j] = list1[j] + list1[i]
            list1[ i]=100
min1 = min(list1)
print(min1)