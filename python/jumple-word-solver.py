def jumble_word(word,dictionary):

    def wrapper(current):
        if len(current)==len(word):
            if current in dictionary:
                print(current)
            return

        for w in word:
            if w not in current:
                wrapper(current+w) 
    wrapper("")
dictionary = {"cat", "act", "tac", "dog", "god", "rat", "tar", "art"}
print(dictionary)
jumble_word("tar",dictionary)