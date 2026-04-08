import sys


def solve():
    # 使用你学到的高铁版输入
    line = sys.stdin.readline().split()
    if not line:
        return
    m, a = map(int, line)

    # 特殊情况：如果第一天或第二天就达标了
    if 1 % m == a:
        print(1)
        return

    # 初始化前两天的值
    f1 = 1  # 第 1 天
    f2 = 1  # 第 2 天
    day = 2  # 当前算到了第 2 天

    # 循环寻找。
    # 停止条件：1. 找到了 a 2. 重新回到了 1, 1（说明开始重复了，找不到了）
    # 为了保险，我们直接设置一个足够大的循环上限（6 * m）
    limit = 5 * m

    while day < limit:
        # 计算新一天的值，并立刻取余（防止数字变得无限大）
        f_next = (f1 + f2) % m
        day += 1

        if f_next == a:
            print(day)
            return

        # 像接力棒一样往后传
        f1 = f2
        f2 = f_next

        # 如果重新回到了 1, 1 且不是开头，说明没戏了
        if f1 == 1 and f2 == 1:
            break

    print("-1")


if __name__ == "__main__":
    solve()