def solve():
    # 1. 快速读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 2. 核心判断函数：能否让所有瓶子的水都 >= x
    def check(x):
        # 遍历 k 个完全独立的分组
        for c in range(k):
            pool = 0  # 记录当前手里攒的“多余的水”
            # 在当前分组内，从左往右遍历 (步长为 k)
            for i in range(c, n, k):
                # a[i] - x 是当前瓶子能提供的盈余(正数) 或 需要的补缺(负数)
                pool += a[i] - x

                # 如果池子里的水变负数了，说明前面的水不够填补当前瓶子的缺口
                # 因为右边的水倒不过来，所以目标 x 无法达成
                if pool < 0:
                    return False
        # 如果所有分组都能顺利从左走到右，说明 x 是可以达成的
        return True

    # 3. 二分模板
    left = 0
    # 上限可以设一个足够大的数，或者当前数组的总和
    right = int(1e15)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid  # mid 是可行的，先记录下来
            left = mid + 1  # 尝试挑战更大的最小值
        else:
            right = mid - 1  # mid 满足不了，目标定太高了，降低标准

    print(ans)


if __name__ == '__main__':
    solve()