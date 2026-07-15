strs=["flower","flow","flight"]
prefix = strs[0]
for word in strs[1:]:
    for i in range(min(len(prefix), len(word))):
     if prefix[i]!=word[i]:
        prefix=prefix[:i]
        break
print(prefix)                     # fl

def longestCommonPrefix(strs):
      prefix=strs[0]
      for word in strs[1:]:
         while not word.startswith(prefix):
            prefix=prefix[:-1]
      return prefix
strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))