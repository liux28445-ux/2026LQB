from collections import Counter

# 1. 读取输入
word = input().strip()

# 2. 统计字母次数（这步保留，因为Counter确实比手写字典简单太多）
count_result = Counter(word)

# ------------------ 把原来的一行拆成下面的简单逻辑 ------------------

# 3. 初始化变量：记录当前最大次数 和 对应的字母
max_count = 0
best_char = ''

# 4. 按 a-z 的顺序遍历26个字母（天然保证字典序！）
for char in 'abcdefghijklmnopqrstuvwxyz':
    # 只有当这个字母在单词里出现过，才进行判断
    if char in count_result:
        current_count = count_result[char]
        # 如果当前字母的次数 严格大于 之前记录的最大次数
        if current_count > max_count:
            # 更新最大次数 和 对应的字母
            max_count = current_count
            best_char = char
            break

# ------------------ 简化逻辑结束 ------------------

# 5. 输出结果
print(best_char)
print(max_count)