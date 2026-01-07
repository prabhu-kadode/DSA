def find(words,word): 
    def getWord(babyword): 
        if babyword in words:
            print(babyword)
            return True
        for w in word:
            if w not  in babyword:
                if getWord(babyword+w):
                    return True
        return False
    getWord("")
        

find(["god","dad","cat"],"tcat")
