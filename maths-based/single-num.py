def findSingleNum():
    nums = [1,1,2,2,3,3,4]
    res = 0
    for n in nums:
        res^=n
    return res
print(findSingleNum())