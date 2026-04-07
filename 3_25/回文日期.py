import datetime


def solve():
   t1= input()
   t1 = datetime.datetime.strptime(t1,'%Y%m%d')

   delta  =datetime.timedelta(days=1)

   t1+=delta

   # 判断找没找到下一个回文日期
   found_date = False

   while True:
       # 转换成字符串
       t2 =datetime.datetime.strftime(t1,'%Y%m%d')
       if t2 == t2[::-1]:
           if not found_date:
               print(t2)
               found_date = True
           if t2[0] == t2[2] and t2[1] == t2[3] and t2[4] == t2[6] and t2[5]==t2[7] and t2[0] != t2[1]:
                print(t2)
                break
       t1+=delta
# 运行代码
if __name__ == '__main__':
    solve()