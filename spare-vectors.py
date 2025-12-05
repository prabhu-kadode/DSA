class SpareVector:
    def __init__(self,data):
        self.filteredData = {i:v for i,v in enumerate(data) if v>0}
        # self.filteredData = {}
        # for index,item in enumerate(data):
        #     if item >0:
        #         self.filteredData[index]=item


s = SpareVector([1,2,0,0,0,0,1,1,1,0,0,2,3,4,0,0,0])
s1 = SpareVector([1,2,0,0,0,0,1,0,0,0,0,2,3,4,3,3,3])

def vectorSpare(v1,v2):
    vectorProduct = []
    if v1.keys() < v2.keys():
        small = v1
        big = v2
    else:
        small = v2
        big = v1
    print(small)
    for i in small:
        print(i)
        if big.get(i):
            vectorProduct.append(small[i]*big[i])
    print(vectorProduct)

        
vectorSpare(s.filteredData,s1.filteredData)
