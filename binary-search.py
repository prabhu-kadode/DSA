def binary_search(arr,target):
    left , right = 0, len(arr)-1

    while left<=right:
        middle = (left+right)//2

        if arr[middle]==target:
            print(f"Item found at index of {middle}")
            return 1
        
        if arr[middle]<target:
            left = middle+1
        else:
            right = middle-1
    
    print(f"Item {target} not found")
    return -1
print(binary_search([1,2,3,4,5,6,7,8,9],10))