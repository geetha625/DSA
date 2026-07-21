'''strs=["flower","flow","flight"]
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
print(longestCommonPrefix(strs))        # fl  '''

# valid anagram

def isAnagram(s,t):
      if len(s)!=len(t):
            return False
      freq1={}
      freq2={}
      for ch in s:
       freq1[ch]=freq1.get(ch,0)+1
      for ch in t:
       freq2[ch]=freq2.get(ch,0)+1
      return freq1==freq2
s="listen"
t="silent"
print(isAnagram(s,t))              # True
