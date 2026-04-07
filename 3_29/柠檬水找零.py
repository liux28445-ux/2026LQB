def lemonade_change(bills: list) -> bool:
    # 初始化我们手里的零钱数量
    five_count = 0  # 5美元钞票的数量
    ten_count = 0  # 10美元钞票的数量

    # 模拟顾客排队一个个来买
    for bill in bills:
        if bill == 5:
            # 顾客给5美元，直接收下
            five_count += 1

        elif bill == 10:
            # 顾客给10美元，必须找零5美元
            if five_count > 0:
                five_count -= 1  # 找出去一张5块
                ten_count += 1  # 收进一张10块
            else:
                # 连一张5块都没有，找不开，直接失败
                return False

        elif bill == 20:
            # 顾客给20美元，贪心策略开始！
            # 优先采用方案A：10 + 5 (赶紧把没用的10块花出去)
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            # 如果没有10块钱，只能被迫采用方案B：5 + 5 + 5
            elif five_count >= 3:
                five_count -= 3
            # 两种方案都凑不齐，找不开，直接失败
            else:
                return False

    # 如果所有顾客都顺利走完循环，说明全都找开了！
    return True


# --- 测试一下 ---
# 场景1：顺利找零
queue1 = [5, 5, 5, 10, 20]
print(f"队列 {queue1} 能否找开? : {lemonade_change(queue1)}")  # 输出 True

# 场景2：遇到刁钻顾客找不开
queue2 = [5, 5, 10, 10, 20]
print(f"队列 {queue2} 能否找开? : {lemonade_change(queue2)}")  # 输出 False