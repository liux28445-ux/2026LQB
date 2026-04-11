h, w = map(int, input().split())
line = '2025' * 50
for i in range(h):
  print(line[i:i+w])