class SpareVector:
    def __init__(self,data):
        self.filteredData = {i:v for i,v in enumerate(data) if v>0}
        # self.filteredData = {}
        # for index,item in enumerate(data):
        #     if item >0:
        #         self.filteredData[index]=item


s = SpareVector([1,2,0,0,0,0,1,1,1,0,0,2,3,4,0,0,0])
s1 = SpareVector([1,2,0,0,0,0,1,0,0,0,0,2,3,4,3,3,3])
class VectorOps:
    def __init__(self,v1,v2):
        self.small = None
        self.big = None
        self.updatbigandsmall(v1,v2)
    def updatbigandsmall(self,v1,v2):
        if len(v1) < len(v2):
            self.small = v1
            self.big = v2
        else:
            self.small = v2
            self.big = v1
    def vectorProduct(self):
        vectorProduct = []
        for i in self.small:
            if self.big.get(i):
                vectorProduct.append(self.small[i]*self.big[i])
        print(vectorProduct)
    def vectorAddtion(self):
        vectorSum = []
        for i in self.small:
            if self.big.get(i):
                vectorSum.append(self.small[i]+self.big[i])
        print(vectorSum)
        
vOps =VectorOps(s.filteredData,s1.filteredData)
vOps.vectorProduct()
vOps.vectorAddtion()