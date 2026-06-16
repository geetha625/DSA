 # reverse array
def reverse(arr):
    return arr[::-1]
print(reverse([1,2,3,4]))       #   [4, 3, 2, 1]

# reverse array without using slicing
def reverse(arr):
    rev=[]
    for num in arr:
        rev=num+rev   or rev.insert(0,num)
    return rev                   # [4, 3, 2, 1]

# find max element
def max_(arr):
    return max(arr)
print(max_([1,2,3,4]))            # 4

# find max without using max
def max_(arr):
    max_=arr[0]
    for num in arr:
        if num>max_:
            max_=num
    return max_
print(max_([11,25,63,34]))             # 63

# find min element
def min_(arr):
    return min(arr)
print(min_([11,25,63,34]))            # 11

# find min element without using min
def min_(arr):
    min_=arr[0]
    for num in arr:
        if num<min_:
            min_=num
    return min_
print(min_([11,25,63,34]))             # 11

# search an element
def search_(arr,target):
    for num in range(len(arr)):
        if arr[num]==target:
            return num
    return -1
print(search_([11,25,63,34],25))          # 1 index

# count even nums
def even_(arr):
    count=0
    for num in arr:
        if num%2==0:
            count+=1   
    return count
print(even_([11,25,63,34]))                           # 1

# checks sum

class Solution:
    def isSorted(self,nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True
obj=Solution()
print(obj.isSorted([1,2,2,3]))              # True

# second largest

def second_largest(nums):
    large_=nums[0]
    second_=float('-inf')
    for num in nums:
        if num>large_:
            second_=large_
            large_=num
        elif num >second_ and num!=large_:
            second_=num
    return second_
print(second_largest([4,23,64,11,54]))         # 54


          

