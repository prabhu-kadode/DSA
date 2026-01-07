a=[1,2,3,3,3,4,5,6]
i=0
j=1
while j<len(a):
    if a[i]!=a[j]:
        i+=1
        a[i]=a[j]
    j+=1
print(a)
print(a[:i+1])