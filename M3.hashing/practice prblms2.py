# count occurences 

arr = [4,5,4,6,5,4]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
print(freq)                                # {4: 3, 5: 2, 6: 1}

# most freq element

arr = [1,1,2,2,2,3]
max_freq=0
ans=-1
for num in arr:
    freq[num]=freq.get(num,0)+1
    if freq[num]>max_freq:
        max_freq=freq[num]
        ans=num
print(ans)                                 # 2

# first repeating element

arr = [10,5,3,4,3,5,6]
seen=set()
for num in arr:
    if num in seen:
       print(num)
       break
    seen.add(num)

