def can_jump(nums):
    max_reach = 0  # 当前能到达的最远下标

    for i in range(len(nums)):

        if i > max_reach:
            return False

        # 贪心选择：更新能到达的最远边界
        # 当前位置 i 加上在该位置能跳跃的最大长度 nums[i]
        max_reach = max(max_reach, i + nums[i])

        # 提前优化：如果最远边界已经能覆盖终点，直接成功
        if max_reach >= len(nums) - 1:
            return True

    return True

nums = [int(x) for x in list(input())]
print(can_jump(nums))  # 输出: False