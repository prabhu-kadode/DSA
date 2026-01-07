arr1 = [2,4,8,9]
arr2 = [1,3,5,6,7]

def mergeTwoSorted():
    i=j=0
    sortedarr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            sortedarr.append(arr1[i])
            i+=1
        else:
            sortedarr.append(arr2[j])
            j+=1
        
    sortedarr.extend(arr1[i:])
    sortedarr.extend(arr2[j:])

    print(sortedarr)

mergeTwoSorted()