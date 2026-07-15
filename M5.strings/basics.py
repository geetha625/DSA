# reverse the string

s="python"
rev=""
for ch in s:
    rev=ch+rev
print(rev)         # nohtyp

# check palindrome

t="madam"
rev=""
org=t
for ch in t:
    rev=ch+rev
if rev==org:
    print(True)
else:
    print(False)       # True

# character frequency

a="banana"
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)                    # {'b': 1, 'a': 3, 'n': 2}

a="banana"
freq={}
for ch in a:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)                  #  {'b': 1, 'a': 3, 'n': 2}
