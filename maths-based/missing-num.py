def findMissingNums():
    nums = [1,2,3,4,5,7,8]
    n = max(nums)
    return n*(n+1)//2 - sum(nums)
print(findMissingNums())

def findMissingNums2():
    nums = [1,2,3,4,5,0,7,8]
    n = len(nums)
    return n*(n+1)//2 - sum(nums)
print(findMissingNums2())
