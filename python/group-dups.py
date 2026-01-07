data = [
    "apple","apple","orange","mango","apple","mango"
]
def groupDups(data):
    combineDups = {}
    for item in data:
        if item in combineDups:
            combineDups[item].append(item)
        else:
            combineDups[item]=[item]
    print(list(combineDups.values()))
groupDups(data)