count =0
for B in range(255):
    for j in range(255):
        if B<j:
            break
        for k in range(255):
            if j<k:
                break
            else:
                count+=1
print( count)

w=0
for i in range(1,256):
  w+=i**2
print(w)