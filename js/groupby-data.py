def groupByData(data):
    maindata = {}
    for item in data:
        for key in item:
            if key in maindata:
                maindata[key].append(item.get(key))
            else:
                maindata[key]=[item.get(key)]
    print(maindata)

data = [
    {
    "name":"prabhu",
    "age":30,
    "city":"banglore"
}, {
    "name":"prabhu1",
    "age":30,
    "city":"mumbai"
}
]
groupByData(data)