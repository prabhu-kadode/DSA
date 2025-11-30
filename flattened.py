def flattenList(n):
    flattenedList = []
    def wrapper(n):
        if not isinstance(n, list):
            flattenedList.append(n)
            return
    
        for i in n:
            wrapper(i)
    wrapper(n)

    return flattenedList


print(flattenList([1, 2, 3, [1, 2, 3],[1,[1,[1,[2,3,4,[4]]]]]]))
print(flattenList([1, 2, 3, [1, 2, 3],[1,[1,[1,[2,3,4,[4]]]]]]))
