# 1.prefix sum array

arr=[2,4,6,8,10]
prefix=[]
curr_sum=0
for num in arr:
    curr_sum+=num
    prefix.append(curr_sum)
print(prefix)    # [2, 6, 12, 20, 30]

# 2.range sum query

arr=[1,2,3,4,5]
left=1
right=3
prefix=[]
curr_sum=0
for num in arr:
    curr_sum+=num
    prefix.append(curr_sum)
range_sum=prefix[right]-prefix[left-1]
print(prefix)                  # [1, 3, 6, 10, 15]
print(range_sum)               # 9

# 3.equilibrium index

arr=[1,7,3,6,5,6]
total_sum=sum(arr)
left_sum=0
for i in range(len(arr)):
    right_sum=total_sum-left_sum-arr[i]
    if left_sum==right_sum:
        left_sum+=arr[i]
print(left_sum)   
