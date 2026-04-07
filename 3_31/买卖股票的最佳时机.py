"""
问题描述：
给你一个整数数组 prices，其中 prices[i] 表示某只股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有一股股票。你也可以先购买，然后在 同一天 出售。
返回你能获得的 最大 利润。

示例：prices = [7, 1, 5, 3, 6, 4]，最大利润是 7。
（在第 2 天买入，第 3 天卖出，赚 4；然后在第 4 天买入，第 5 天卖出，赚 3。总利润 4 + 3 = 7）
"""
def maxTime(prices):
    money = 0
    for i in range(1,len(prices)):
        if prices[i] -prices[i-1]:
            money += prices[i] - prices[i-1]

    return money




if __name__ == '__main__':
    prices =[int(i) for i in input()]
    print(maxTime(prices))

