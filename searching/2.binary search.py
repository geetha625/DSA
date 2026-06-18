def bin_search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
nums=[10,20,30,40,50]
target=30
res=bin_search(nums,target)
print(res)                                       # 2

def bin_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
arr=[10,20,30,40,50]
target=50
res=bin_search(arr,target)
if res!=-1:
    print("element is found at : ",res)
else:
    print("element not found")                      # element is found at :  4


def first_occurrence(arr, k):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==k:
            ans=mid
            right=mid-1
        elif arr[mid]<k:
            left=mid+1
        else:
            right=mid-1
    return ans
arr=[1,2,2,2,3,4]
k=2
res=first_occurrence(arr, k)
print(res)                                  # 1

def last_occurence(arr,k):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==k:
            ans=mid
            left=mid+1
        elif arr[mid]<k:
            left=mid+1
        else:
            right=mid-1
    return ans
arr=[1,2,2,2,3,4]
k=2
res=last_occurence(arr,k)
print(res)



