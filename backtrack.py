# def backtrack(word):
#     def wrapper(char):
#         if len(char)==3:
#             print(char)
#             return
        
#         for i in word:
#             wrapper(char+i)
#     wrapper("")
# backtrack("abc")

def backtrack(word):
    def wrapper(char):
        if char:
            print(char)
        if len(char)==len(word):
            return 
        for i in word:
            wrapper(char+i)
    wrapper("")
backtrack("abc")
    
