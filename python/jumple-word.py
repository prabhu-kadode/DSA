def find(words,word):
    
    for i in words:
        sortedI = sorted(i)
        sortedWord = sorted(word)
        
        if sortedI== sortedWord:
            return i
    return "Not found"

print(find(["god","dad","cat"],"dog"))

