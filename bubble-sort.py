nums = [8,5,4,6,1,2,9,7,36,2,1,2]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)
