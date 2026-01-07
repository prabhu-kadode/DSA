nums = [5,2,6,7,8,9,2,4,5,6,20]

largest = nums[0]
secondl = None

for i in range(1,len(nums)):
    item = nums[i]
    if item > largest:
        secondl = largest
        largest = item
    else:
        secondl = item

print(largest,secondl)
    