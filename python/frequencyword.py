def findFrequence(l):
    dickt = {}
    for i in l:
        if i in dickt:
            dickt[i]=dickt[i]+1
        else:
            dickt[i]=1
    print(dickt)
findFrequence(['a','b','c','a','a','d','d'])