
arr = [1,2,3,4,5,6,7]

roatatedArr = []

for i in range(3):
    reverse = len(arr)-1-i
    roatatedArr.insert(0,arr[reverse])
roatatedArr.extend(arr[:reverse])
print(roatatedArr)

arr = [1,2,3,4,5,6,7]
k = 3
k %= len(arr)
print(k)
print(arr[-k:]+arr[:-k])

rotatedArr = arr[-k:] + arr[:-k]
print(rotatedArr)