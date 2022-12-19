from abc import ABC, abstractmethod

class abstract(ABC):
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

class Waktu(abstract):
    Hour = 0
    Minute = 0
    Second = 0
    
    def __init__(self, Hour, Minute, Second):
        self.__Hour = Hour
        self.__Minute = Minute
        self.__Second = Second

    def getHour(self):
        return self.__Hour
   
    def getMinute(self):
        return self.__Minute

    def getSecond(self):
        return self.__Second

    def setHour(self, input):
        self.__Hour = input
    
    def setMinute(self, input):
        self.__Minute = input
    
    def setSecond(self, input):
        self.__Second = input
        
    def display(self):
        if clock.__Hour <= 24 and clock.__Minute <= 60 and clock.__Second <= 60:
            return "{} : {} : {}".format(clock.getHour(),clock.getMinute(),clock.getSecond())
        else:
            return "Format clock salah!"
    
Hour = int(input("masukkan jam: "))
Minute = int(input("masukkan menit: "))
Second = int(input("masukkan detik: "))

clock = Waktu(Hour, Minute, Second)
print(clock.display())