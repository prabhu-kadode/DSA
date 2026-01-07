list1= [
    
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

n = len(list1)
j= len(list1[0])
newitem = []
for i in range(n):
    bucket = []
    for m in range(j):
        ind = j-m
        bucket.append(list1[ind-1][i])
    newitem.append(bucket)

print(newitem)
        
    