# 读取输入
n = int(input())
# 定义循环字符串
base = "2026"
# 逐行输出
for i in range(1, n + 1):
    # 生成第i行：循环取base的字符，取i个
    line = ""
    for k in range(i):
        line += base[k % 4]
    print(line)