def hello():
    words = ["tan","nat","eat","tea","cufk","kucf","hello","loleh"]
    for i in words:
        print(i.capitalize())
    group = {}
    for word in words:
        t=tuple(sorted(word))
        if t in group:
            group[t].append(word)
        else:
            group[t]=[word]
            
    return group.values()
        
for i in hello():
    print(i)


