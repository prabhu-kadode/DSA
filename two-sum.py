def twosum():
    target = 15
    seen = {}
    for i, item in enumerate([1,2,3,4,5,6,7,8]):
        
        compliment = target-item
        
        if compliment in seen:
            return [seen[compliment],i]
        
        seen[item]=i
print(twosum())