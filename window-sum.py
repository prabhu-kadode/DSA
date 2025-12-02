nums = [2,3,4,1,2,3,4,9,9,5,5,6]

k = 2
start = 0
total = 0
best = 0

# initial window sum
for i in range(k):
    total += nums[i]

best = total

while k < len(nums):
    total = total + nums[k] - nums[start]
    start += 1
    k += 1

    if total > best:
        best = total

print("max window sum =", best)
