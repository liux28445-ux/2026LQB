n = int(input())
a = list(map(str, input().split()))

cnt = [0] * 6
ans = 0

# 统计每个数字中 '6' 的数量
for i in a:
    c = i.count('6')
    if c >= 6:
        ans += 1
    else:
        cnt[c] += 1  # 直接用索引，超级快

# 下面逻辑完全不变！
# 5 + 1
count = min(cnt[5], cnt[1])
ans += count
cnt[5] -= count
cnt[1] -= count

# 剩下的 5 当作 4
cnt[4] += cnt[5]

# 4 + 1 + 1
count = min(cnt[4], cnt[1] // 2)
ans += count
cnt[4] -= count
cnt[1] -= 2 * count

# 4 + 2
count = min(cnt[4], cnt[2])
ans += count
cnt[4] -= count
cnt[2] -= count

# 剩下的 4 当作 3
cnt[3] += cnt[4]

# 3 + 2 + 1
count = min(cnt[3], cnt[2], cnt[1])
ans += count
cnt[3] -= count
cnt[2] -= count
cnt[1] -= count

# 3 + 3
count = cnt[3] // 2
ans += count
cnt[3] -= count * 2

# 剩下的 3 当作 2
cnt[2] += cnt[3]

# 2 + 2 + 2
ans += cnt[2] // 3

print(ans)