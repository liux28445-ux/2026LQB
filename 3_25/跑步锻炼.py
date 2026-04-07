import datetime

start_time= datetime.datetime(2000, 1, 1)
end_time = datetime.datetime(2000, 10, 1)

delta = datetime.timedelta(days=1)
count = 0
while True:
    if start_time <= end_time:
        if start_time.weekday() == 0 or start_time.day == 1 :
            count += 2
        else:
            count += 1
        start_time += delta
    else:
        break
print(count)

