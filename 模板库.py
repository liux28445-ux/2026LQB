# collections：高级数据结构合集
# deque (双端队列)何时使用： 广度优先搜索 (BFS)、滑动窗口、单调队列。
# 优势： 左右两端弹出/插入的时间复杂度都是 $O(1)$，完美替代 list.pop(0)
from collections import deque
q = deque([1, 2, 3])
q.append(4)      # 右入队: deque([1, 2, 3, 4])
q.appendleft(0)  # 左入队: deque([0, 1, 2, 3, 4])
q.popleft()      # 左出队: 0

# defaultdict (默认字典)
# 何时使用： 图论建图（邻接表）、按照特定规则分组。
# 优势： 自动处理空键，省去 if key not in d: 的繁琐判断。
from collections import defaultdict
graph = defaultdict(list)
graph['A'].append('B') # A 节点连接到 B，不需要提前声明 graph['A'] = []

# Counter (计数器)
# 何时使用： 统计字符/数字出现频率、找众数、判断异位词。
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange']
cnt = Counter(words)
print(cnt['apple']) # 输出 2
print(cnt.most_common(1)) # 输出频率最高的 1 个元素: [('apple', 2)]

#heapq：优先队列 / 堆
# 何时使用： 贪心算法（每次取最小/最大）、Dijkstra 最短路径、Top-K 问题、合并多个有序链表。
# 注意： Python 只有小根堆。如果需要大根堆，插入时将数字取相反数（乘 -1），弹出后再恢复
import heapq
nums = [5, 1, 8, 3]
heapq.heapify(nums)       # 原地建堆 (O(N)): [1, 3, 8, 5]
heapq.heappush(nums, 2)   # 插入元素 (O(logN))
min_val = heapq.heappop(nums) # 弹出并返回最小值 1 (O(logN))

# bisect：二分查找
# 何时使用： 在有序数组中找插入位置、找上下边界。
import bisect
nums = [1, 3, 3, 3, 5]
# lower_bound: 找第一个 >= 3 的位置
print(bisect.bisect_left(nums, 3))  # 输出: 1
# upper_bound: 找第一个 > 3 的位置
print(bisect.bisect_right(nums, 3)) # 输出: 4

# cmp_to_key (自定义排序)
# 何时使用： 题目要求奇怪的排序规则（比如：两个数字 x 和 y，如果字符串拼接 x+y > y+x，则 x 排在前面）。
from functools import cmp_to_key
def custom_sort(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1 # x 应该排在 y 前面
    return 1
nums = [3, 30, 34, 5, 9]
nums.sort(key=cmp_to_key(custom_sort))

# math：底层数学运算
# 常见函数：
import math
math.gcd(12, 18)     # 最大公约数: 6
math.lcm(12, 18)     # 最小公倍数: 36 (Python 3.9+)
math.factorial(5)    # 阶乘: 120
math.comb(5, 2)      # 组合数 (C_5^2): 10
math.ceil(2.3)       # 向上取整: 3
ans = math.inf       # 初始化最小值的比较基准: 正无穷

# itertools：暴力枚举与迭代
# 何时使用： 当数据范围很小（如 $N \le 10$），直接暴力生成所有可能的情况。
import itertools
# 全排列 (生成密码、路径枚举)
list(itertools.permutations([1, 2, 3]))
# 组合 (不考虑顺序的抽取)
list(itertools.combinations([1, 2, 3, 4], 2))
# 前缀和快捷生成
list(itertools.accumulate([1, 2, 3, 4])) # [1, 3, 6, 10]

# fractions：分数精确计算
# 何时使用： 遇到浮点数精度丢失问题，或者题目要求输出严格的最简分数形式时。
from fractions import Fraction
f = Fraction(10, 8) # 自动化简为 5/4
print(f.numerator)  # 分子: 5
print(f.denominator)# 分母: 4

import heapq

nums = [5, 1, 8, 3]
heapq.heapify(nums)       # 建堆 → [1, 3, 8, 5]（最小值在索引0）

# ✅ 优势：快速获取最小值 O(1)，插入/删除 O(log n)
min_val = nums[0]         #  peek: 1（不删除）
min_val = heapq.heappop(nums)  # 弹出最小值 → 1
heapq.heappush(nums, 2)   # 插入元素，自动调整堆结构

# ❌ 劣势：只能快速访问最小值，不能随机访问
