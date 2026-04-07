"""
核心思想：
    "暴力破解"。不重不漏地列举出所有可能的情况，一一验证是否满足题目条件。
痛点：
    自己写多重 for 循环不仅容易出错，而且代码冗长。
Python 杀手锏：
    itertools 库。它是蓝桥杯中处理枚举题目的“外挂”。
"""

import itertools

# 从1 到 3 的数字中选两个数字进行全排列
item = [1,2,3]
# 用于处理有顺序要求的枚举（例如：排队问题、密码生成）。
# permutations(可迭代对象，选取数量)
for i in itertools.permutations(item,2):
    print(i)
    """
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 3)
    (3, 1)
    (3, 2)
    """
print('-' * 20)
# 用于处理无顺序要求的枚举（例如：从班级里抽 3 个人打扫卫生）。
# 从 1, 2, 3 中选 2 个数字进行组合（(1,2) 和 (2,1) 算同一种）
for c in itertools.combinations(item,2):
    print(c)
    """
    (1, 2)
    (1, 3)
    (2, 3)
    """

print('-' * 20)

# 笛卡尔积（替代多重循环）：itertools.product
# 相当于：for i in [1, 2]: for j in ['A', 'B']:
for i in itertools.product([1,2,3],['A','B']):
    print(i)
    """
    (1, 'A')
    (1, 'B')
    (2, 'A')
    (2, 'B')
    (3, 'A')
    (3, 'B')
    """
print('-' * 20)
for i in itertools.product(range(1,5),range(1,6)):
    print(i)