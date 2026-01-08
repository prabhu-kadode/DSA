def find_valid_bracktes(str):
    
    stack = []
    brackDict= {"}":"{",")":"(","]":"["}

    for i in str:
        if i in brackDict.values():
            stack.append(i)
        elif i in brackDict:
            if not stack or stack[-1]!=brackDict[i]:
                return False
            stack.pop()
    result = f"the string{str} is valid" if len(stack)==0 else f"the string is {str} is invalid"
    print(result)
    return len(stack)==0
print(find_valid_bracktes("(())"))
