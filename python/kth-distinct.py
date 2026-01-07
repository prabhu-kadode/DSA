def find_kth_distinct(k=3):
    nums = [1,2,1,3,3,2,4,5,6,6,7]
    hashmap = {}
    count = 0
    for i in nums:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    for i in hashmap:
    
        if hashmap[i]<=1:
            count+=1
            if count==k:
                return i
    return None
        
        

print(find_kth_distinct())
        