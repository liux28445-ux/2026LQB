count = 0 # 注释说：求非诗意数字的个数 (这里其实写反了)
for i in num:
    while i > 2:
        if i % 2 == 1:
            count += 1  # 遇到奇数因子，说明它有“诗意”，count 加 1
            break
        else:
            i //= 2
print(len(num) - count) # 总数减去“诗意”的个数，得出需要删除的“非诗意”个数