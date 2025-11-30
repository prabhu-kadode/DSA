def findPattern(sentence,word):
    start = 0
    end= len(word)
    for i in range(len(sentence)-len(word)+1):
        extracted = sentence[start:end]
        if extracted==word:
            print("found",word,extracted)
            return
        start+=1
        end+=1
        print(start)
    print("not found")
findPattern("hello how","hello")
print(10-4+1)
