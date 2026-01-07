def find(words,word):
    def getWord(babyword,word):
       
        if babyword in words:
            print("found",babyword) 
            return True
        for i,c in enumerate(word):
            if getWord(babyword+c,word[:i]+word[i+1:]):
                return True
        return False
    if getWord("",word):
        print("found")
    else:
        print("Not found")
print(find(["god","dad","cat"],"catt"))
