''' FIXED SIZED SLIDING WINDOW '''

# Print the sum of every window of size 3.

arr = [1,2,3,4,5]
k = 3
window_sum=sum(arr[:k])
print(window_sum)
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    print(window_sum)                                 # 6,9,12

# Find the maximum sum window.

arr = [2,1,5,1,3,2]
k = 3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)                                        # 9

# Find the maximum sum subarray of size 3.

arr = [4,2,1,7,8,1,2,8]
k = 3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)                                       # 16

arr = [4,2,1,1,2,8]
k = 3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)   

''' VARIABLE SIZED SLIDING WINDOW '''

# Find the length of the longest subarray whose sum is ≤ 8.
arr = [1,2,3,4,2]
limit = 8
left=0
window_sum=0
max_length=0
for right in range(len(arr)):
    window_sum+=arr[right]
    while window_sum>=limit:
        window_sum-=arr[left]
        left+=1
    max_length=max(max_length,right-left+1)
print(max_length)                                   # 3
  
# Find the smallest subarray whose sum is at least 7.

arr = [2,3,1,2,4,3]
target = 7
left=0
window_sum=0
min_length=float("inf")
for right in range(len(arr)):
    window_sum+=arr[right]
    while window_sum>=target:
        min_length=min(min_length,right-left+1)
        window_sum-=arr[left]
        left+=1
print(min_length)                                 # 2

# longest substring
s="abcabc"
last_seen={}
left=0
max_length=0
for right in range(len(s)):
    if s[right] in last_seen:
        left=max(left,last_seen[s[right]]+1)
        max_length=max(max_length,right-left+1)
print(max_length)
