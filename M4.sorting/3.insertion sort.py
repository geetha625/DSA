arr=[5,2,8,1]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)                                  # [1, 2, 5, 8]

''' time complexity if sorted : best case : o(n)
    time complexity if not sorted : worst case : o(n2)'''