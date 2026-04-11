import os
import sys

# 请在此输入您的代码

n = int(input())
for _ in range(n):
  data = input()
  n = len(data)
  s = ["l","q","b"]
  left = 0
  right = n-1
  while left < right:
    if data[right] == data[left]:
      right -= 1
      left += 1
    elif data[right] in s:
      right -= 1
    else:
      break
  if left >= right:
    print("Yes")
  else:
    print("No")