class Garden():
    def __init__(self, SIZE, nTanaman, mGardenName, pArrList, hasilPanen):
        self.__SIZE = 10
        self.__nTanaman = 0
        self.__mGardenName = "pName"
        self.__pArrList = [10]
        self.__hasilPanen = hasilPanen
    
    def addPlant(self, Plant):
        if(self.__nTanaman < self.__SIZE):
            self.__pArrList.add(Plant)
            self.__nTanaman += 1
            return True
        else:
            return False
    
    def harvestPlant(self):
        tmpN = 0
        i = 0

        while((self.__pArrList != None) and (i < self.__pArrList.size())):
            a