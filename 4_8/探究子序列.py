def solve(N, k, num):
    stack = []  # 这就是我们的“队伍”

    for x in num:
        # 如果 1. 队伍不空 2. 还有名额 3. 新来的比队尾大
        while stack and k > 0 and stack[-1] < x:
            stack.pop()  # 开除队尾
            k -= 1  # 消耗一个名额
        stack.append(x)  # 新来的入队

    # 如果名额还没用完（比如数字是 9876），就从后面直接砍掉剩下的
    if k > 0:
        stack = stack[:-k]

    print(''.join( stack))

if __name__ == '__main__':
    N,k=map(int,input().split())
    num =  input().strip()
    solve(N, k, num)
