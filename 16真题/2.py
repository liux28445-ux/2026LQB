c = 0
for i in range(2000,20250413):
    x =str(i)
    if x.count('0')>=1 and x.count('5') >=1 and x.count('2')>=2:
          c+=1
print(c)