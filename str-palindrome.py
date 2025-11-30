def findPalindrome(str):
    left =0
    right= len(str)-1
    while left<right:
        if str[left]!=str[right]:
           break
        left+=1
        right-=1
    else:
        return 1
    
    return -1
print(findPalindrome("aabbaa"))
