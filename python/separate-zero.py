def separatezeros():
    nums = [0,1,0,0,2,0,1,1,1,0,2]
    zero_index= 0
    non_zero_index= 0
    for _ in nums:
        if nums[non_zero_index]==0:
            nums[zero_index],nums[non_zero_index]=nums[non_zero_index],nums[zero_index]
            zero_index+=1
            non_zero_index+=1
        else:
            non_zero_index+=1
    
    print(nums)
separatezeros()