import itertools


def solve_mixed_fraction():
    # 假设输入 N = 100
    N = int(input())
    # N = 100

    count = 0
    # 生成 1 到 9 的字符列表，方便后面直接拼成字符串
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 1. 枚举所有全排列
    for p in itertools.permutations(nums):
        # 把当前的排列拼成一个完整的 9 位字符串 (比如 "369258714")
        s = "".join(p)

        # 2. 用两重循环设定切片的位置 i 和 j
        # i 代表第一刀的位置 (留给 a 至少 1 位数字，所以 i 从 1 开始)
        for i in range(1, 8):
            # j 代表第二刀的位置 (留给 b 至少 1 位，c 至少 1 位)
            for j in range(i + 1, 9):

                # 3. 字符串切片发力！切出三段并转成整数
                a = int(s[:i])  # 比如 "3"
                b = int(s[i:j])  # 比如 "69258"
                c = int(s[j:])  # 比如 "714"

                # 4. 代入防精度丢失的乘法公式验证
                if b == (N - a) * c:
                    count += 1
                    # print(f"{N} = {a} + {b}/{c}") # 取消注释可以看具体的解

    print(count)


solve_mixed_fraction()  # 输出: 11