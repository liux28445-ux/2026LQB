h,w = map(int,input().split())
x = "2025"*(w//4+1)
x = x[0:w]
for _ in range(h):

    print(x)
    x = x[1:]+x[0]