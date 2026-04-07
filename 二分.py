def middle(num,c):
    left = 0
    right = len(num) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if num[mid] == c:
            return  mid
        if num[mid] < c:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(nums, target):
    # 搜索区间为左闭右开 [left, right)
    left = 0
    right = len(nums)

    while left < right:  # 终止条件是 left == right
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1  # 目标仍在右侧
        else:
            right = mid  # nums[mid] >= target，当前 mid 可能是答案，也可能在左侧，所以 right 缩到 mid

    # 循环结束后 left == right
    return left


# 测试
nums = [1, 2, 2, 2, 3]
print("第一个 >= 2 的索引是:", lower_bound(nums, 2))  # 输出: 1
print("第一个 >= 4 的索引是:", lower_bound(nums, 4))  # 输出: 5 (越界，表示所有元素都小于 4)
if __name__ == '__main__':
    # 1. 读取第一行输入，并用 list() 将 map 对象转换为列表
    # 例如输入: 1 3 5 7 9
    nums = list(map(int, input().split()))

    # 2. 读取第二行输入，作为我们要查找的单一目标值 c
    # 例如输入: 5
    target = int(input())

    # 3. 调用函数并打印结果
    print(middle(nums, target))