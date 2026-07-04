def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for num in arr[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quickSort(left)+[pivot]+(right)
print(quickSort([7,2,9,1,5,8]))                     # [1, 2, 5, 7, 8, 9]

s = "abba"
left=0
seen=set()
max_length=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    max_length=max(max_length,right-left+1)
print(max_length)                                 # 2

s = "abccbaa"
left=0
seen=set()
max_length=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[right])
        left+=1
    seen.add(s[right])
    max_length=max(max_length,right-left+1)
print(max_length)                                   