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

arr = [4,2,1,,1,2,8]
k = 3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum=window_sum-arr[i-k]+arr[i]
    max_sum=max(max_sum,window_sum)
print(max_sum)                                       