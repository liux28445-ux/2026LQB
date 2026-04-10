n = int(input())
s1 = []
s2 =  []
len1 = n//2
t=0
for _ in range(n):
    s1.append(int(input()))
for _ in range(n):
    s2.append(int(input()))
s1.sort()
s2.sort()
for a,b in zip(s1,s2):
    t+=abs(b-a)
print( t)