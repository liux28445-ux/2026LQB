def prefix_sum_demo(nums, queries):
    n = len(nums)
    # 构建前缀和数组，长度为 n+1，pre[0] = 0
    # pre[i] 表示 nums[0] 到 nums[i-1] 的累加和
    pre = [0] * (n + 1)

    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]

    print(f"原数组: {nums}")
    print(f"前缀和: {pre}")

    # 处理查询 queries = [[L1, R1], [L2, R2]] (闭区间，索引从 0 开始)
    results = []
    for L, R in queries:
        # 因为 pre 整体向右偏移了一位，所以区间 [L, R] 的和是 pre[R+1] - pre[L]
        subarray_sum = pre[R + 1] - pre[L]
        results.append(subarray_sum)

    return results


# 测试
nums = [3, 1, 4, 1, 5]
queries = [[0, 2], [1, 4]]
print("区间和:", prefix_sum_demo(nums, queries))
# 输出: 区间和: [8, 11]  (即 3+1+4=8, 1+4+1+5=11)

