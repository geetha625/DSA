# contains duplicates

arr = [1,2,3,1]
seen=set()
for ch in arr:
    if ch in seen:
        print(True)
        break
    seen.add(ch)
else:
        print(False)               # True

# count frequency

arr=[1,1,2,3,2,1]
freq={}
for num in arr:
     freq[num]=freq.get(num,0)+1
print(freq)                                  # {1: 3, 2: 2, 3: 1}

# first non-repeating chars

s="aabbcde"
freq={}
for ch in s:
     freq[ch]=freq.get(ch,0)+1
for ch in s:
     if freq[ch]==1:
          print(ch)
          break
print(freq)
# c
# {'a': 2, 'b': 2, 'c': 1, 'd': 1, 'e': 1}

# common elements

arr1 = [1,2,3,4]
arr2 = [3,4,5,6]
set1=set(arr1)
common=set()
for num in arr2:
     if num in set1:
          common.add(num)
print(common)                             # {3, 4}
