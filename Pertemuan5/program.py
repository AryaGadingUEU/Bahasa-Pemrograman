# NAMA: ARYA GADING
# NIM: 20210801321
# PBO PERTEMUAN SESI 5

class Product:
    #Class Attributes
    mProductID = None
    mProductName = None
    mPrice = None
    mQuantity = None
    
    #Instance Attributes / Initializer / Constructor
    def __init__(self, mProductID, mProductName, mPrice, mQuantity):
        self.__productID = mProductID
        self.__productName = mProductName
        self.__Price = mPrice
        self.__Qty = mQuantity
    
    #Fungsi Setter
    def setmProductID(self, input):
        self.__productID = input
    
    def setmProductName(self, input):
        self._productName = input

    def setmPrice(self, input):
        self._Price = input

    def setmQuantity(self, input):
        self._Qty = input
    
    #Fungsi Getter
    def getmProductID(self):
        return self.__productID
    
    def getmProductName(self):
        return self.__productName

    def getmPrice(self):
        return self.__Price
    
    def getmQty(self):
        return self.__Qty
    
    
    def display(self):
        return "ID PRODUK: {}\nNAMA PRODUK: {}\nHARGA: {}\nJUMLAH: {}\n".format(self.__productID,self.__productName,self.__Price,self.__Qty)

#instantiate Product class
P = Product(0, 'Aqua Botol', 5000, 3) 

print(P.display())