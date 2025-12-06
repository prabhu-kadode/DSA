def findLargest(items):
    largest = items[0]

    for item in items:
        largest = max(largest,item)
    return largest
def getkthLargest(items,k):
    kthlargestItem = None
    items = items
    for _ in range(k):
        if kthlargestItem is not None:
            items.remove(kthlargestItem)
        kthlargestItem= findLargest(items)
    return kthlargestItem
print(getkthLargest([1,2,3,4,5,6,7],4))



