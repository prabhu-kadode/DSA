def reverseString(mystr):
    left =0
    right= len(mystr)-1
    copystr = list(mystr)
    while left<right:
       copystr[left],copystr[right]=copystr[right],copystr[left]
       left+=1
       right-=1
    return "".join(copystr)
print(reverseString("hello"))