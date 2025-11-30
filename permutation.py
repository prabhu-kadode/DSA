# def backtrack(n):
#     result = []
#     def wrapper(current):
        
#         if len(current)==len(n):
#             result.append(current[:])
#             return
        
#         for i in n:
#             if i not in current:
#                 current.append(i)
#                 wrapper(current)
#                 current.pop()
        
#     wrapper([])
#     print(result)
#     print(len(result))

# print(backtrack([1,2,3,4]))

def backtrack(word):
    def wrapper(current):
        if len(word)==len(current):
            print(current)
            return
        for w in word:
           
            if w not in current:
                wrapper(current+w)
                current[:-1]
    wrapper("")
backtrack("abc")
            
