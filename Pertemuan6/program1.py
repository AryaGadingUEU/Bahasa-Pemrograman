#Nama       : Arya Gading
#NIM        : 20210801321
#Tugas Sesi : 6

from abc import ABC, abstractmethod

class IsiJam(ABC): #Abstraksi
    @abstractmethod
    def setHour(self, input):
        self.__Hour = input
    
    @abstractmethod
    def setMinute(self, input):
        self.__Minute = input

    @abstractmethod
    def setSecond(self, input):
        self.__Second = input

    @abstractmethod
    def getHour(self):
        return self.__Hour

    @abstractmethod
    def getMinute(self):
        return self.__Minute
    
    @abstractmethod
    def getSecond(self):
        return self.__Second

class Jam(IsiJam):
    Hour = 0
    Minute = 0
    Second = 0
    
    #Konstruktor
    def __init__(self, Hour, Minute, Second):
        self.__Hour = Hour
        self.__Minute = Minute
        self.__Second = Second
    
    #Setter (Enkapsulasi)
    def setHour(self, input):
        self.__Hour = input
    
    def setMinute(self, input):
        self.__Minute = input
    
    def setSecond(self, input):
        self.__Second = input

    #Getter (Enkapsulasi)
    def getHour(self):
        return self.__Hour
   
    def getMinute(self):
        return self.__Minute

    def getSecond(self):
        return self.__Second
        
    def display(self):
        if clock.__Hour <= 23 and clock.__Minute <= 59 and clock.__Second <= 59:
            return "Sekarang sudah menunjukkan clock: Hour {}, {} Minute, {} Second".format(clock.getHour(),clock.getMinute(),clock.getSecond())
        else:
            return "Mohon Maaf, format clock yang dimasukkan menyalahi aturan!"
    
Hour = int(input("Hour berapa sekarang (0 - 23): "))
Minute = int(input("Minute berapa sekarang (0 - 59): "))
Second = int(input("Second berapa sekarang (0 - 59): "))

clock = Jam(Hour, Minute, Second)
print(clock.display())