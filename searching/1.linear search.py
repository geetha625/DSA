def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50]
target=30
res=linear_search(arr,target)
print(res)                            # 2

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[11,22,33,55,44]
target=25
res=linear_search(arr,target)
if res!=-1:
    print("element found at :",res)
else:
    print("element not found")
