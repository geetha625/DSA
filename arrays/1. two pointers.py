
# reverse a string

def reverseString(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
s=["h","e","l","l","o"]
#print(reverseString(s))                    # ['o', 'l', 'l', 'e', 'h']
print("".join(reverseString(s)))    # olleh

# palindrome

def palindromeString(s):
    left=0
    right=len(s)-1
    while left<right:
       if s[left]!=s[right]:
          return False
       left+=1
       right-=1
    return True
s="madam"
print(palindromeString(s))     # True




