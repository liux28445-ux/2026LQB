# 字符串切片
s = 'hello world'

# 包左不保右
print(s[:2])

print(s[::-1])

# 判断是否为回文串
word = "racecar"
if word == word[::-1]:
    print("是回文！")

# 分割 split() 与 拼接 join()
data = '2024-01-01'
new_data=data.split()
print(data.split('-'))

# join ():将列表中的元素用指定字符拼接成字符串
# 注意：列表里的元素必须都是字符串！
print('-'.join(new_data))

print('-' * 10)

"""
datetime.date(year, month, day): 表示一个具体的日期。
datetime.timedelta(days=n): 表示一段时间的跨度（用来加减天数）
"""

# 实战：计算 2000 年 1 月 1 日 到 2020 年 1 月 1 日 之间，有多少个星期一？
"""
datetime.timedelta：时间差（模拟算法的核心！）
timedelta 代表的是一段持续的时间（比如 3天、2小时）。
在模拟时间的流逝时，它不可或缺。注意：它可以和 date 或 datetime 对象直接进行加减法。

代码案例:
    start_date = datetime.date(2024, 1, 1)
    
    # 定义一个 10 天的时间跨度
    delta = datetime.timedelta(days=10)
    
    # 计算 10 天后是哪一天
    future_date = start_date + delta
    print("10天后是:", future_date) # 输出: 2024-01-11
    
    # 计算两个日期相差多少天
    d1 = datetime.date(2024, 5, 1)
    d2 = datetime.date(2024, 1, 1)
    diff = d1 - d2
    print("相差天数:", diff.days) # 输出: 121
"""
import datetime
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 1, 1)

#
delta = datetime.timedelta(days=1)

count = 0
# 3. 开始模拟时间的推移（枚举每一天）
while start_date<=end_date:
    # weekday() 返回 0-6，0 代表星期一，6 代表星期日
    if start_date.weekday() == 0:
        count += 1
    start_date += delta

print(f'2000-01-01 到 2020-01-01 之间有{count}个星期一')

"""
题目给你的输入往往是字符串（如 "20231024" 或 "2023-10-24"），你需要把它变成 datetime 对象才能做加减法；计算完后，又需要按特定格式输出。
这时候就需要用到以下两个方法。
记住常见的格式化符号：
    %Y：四位数的年份 (2024)
    %m：两位数的月份 (05)
    %d：两位数的日期 (20)
    %H：24小时制的小时 (14)
    %M：分钟 (30)
    %S：秒 (00)
"""
import datetime

date = "2023-10-24"

# strptime：字符串 解析为 时间 (String Parse Time)
p_date = datetime.datetime.strptime(date,'%Y-%m-%d')
print(p_date) # 输出: 2023-10-24 00:00:00
print(type(p_date)) # 输出: <class 'datetime.datetime'>

# strftime：时间 格式化为 字符串 (String Format Time)
my_date = datetime.datetime(2024, 5, 1)
print(my_date.strftime('%Y%m%d')) # 输出: 20240501

# 转换成带中文的格式
custom_string = my_date.strftime("%Y年%m月%d日")
print(custom_string) # 输出: 2024年05月20日