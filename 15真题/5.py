def calculate_minimum_operations():
    # 读取输入的整数n，表示数组的长度
    n = int(input())
    # 读取输入的数组元素，并将其转换为整数列表
    a = list(map(int, input().split()))

    # 初始化操作次数为0
    cnt = 0
    # 初始化左右指针，分别指向数组的开始和结束位置
    left, right = 0, n - 1

    while left < right:
        # 如果左右指针指向的元素相等，直接向中间移动指针
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            # 计算左右指针指向元素的差值
            diff = a[right] - a[left]

            tag = abs(diff)
            cnt += tag

            # 判断左右指针相邻元素的大小关系，都小于或者都大于
            if (a[left] < a[right] and a[left + 1] < a[right - 1]) or (
                    a[left] > a[right] and a[left + 1] > a[right - 1]):
                # 根据差值更新相 邻元素的值，这是核心
                if a[left] < a[right]:
                    a[left + 1] = min(tag + a[left + 1], a[right - 1])
                else:
                    a[right - 1] = min(tag + a0[right - 1], a[left + 1])

            # 移动指针
            left += 1
            right -= 1

    return cnt


result = calculate_minimum_operations()
print(result)