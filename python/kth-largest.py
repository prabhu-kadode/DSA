import heapq

def kth_largest(nums, k):
   min_heap = []

   for i in nums:
      heapq.heappush(min_heap,i)
      if len(min_heap)>k:
         heapq.heappop(min_heap)

   return min_heap[0]

print(kth_largest([67,8,7,10,11,2,3],4))
