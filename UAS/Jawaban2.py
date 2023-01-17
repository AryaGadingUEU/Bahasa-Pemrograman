class Plant:
    def __init__(self, name):
        self.__name = name
        self._tinggi = 0
    
    def set_tinggi(self, tinggi):
        self._tinggi = tinggi
    
    def get_tinggi(self):
        return self._tinggi
    
    def get_name(self):
        return self.__name

class Mawar(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color
    
    def get_color(self):
        return self.__color

class Melati(Plant):
    def __init__(self, name, scent):
        super().__init__(name)
        self.__scent = scent
    
    def get_scent(self):
        return self.__scent

class Anggrek(Plant):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size
    
    def get_size(self):
        return self.__size

mawar = Mawar("Mawar", "merah")
mawar.set_tinggi(100)
print(f"{mawar.get_name()} mempunyai tinggi {mawar.get_tinggi()}cm and berwarna {mawar.get_color()}")

melati = Melati("Melati", "wangi")
melati.set_tinggi(50)
print(f"{melati.get_name()} mempunyai tinggi {melati.get_tinggi()}cm dan {melati.get_scent()} harumnya")

anggrek = Anggrek("Anggrek", "besar")
anggrek.set_tinggi(70)
print(f"{anggrek.get_name()} mempunyai tinggi {anggrek.get_tinggi()} dan ukurannya {anggrek.get_size()}...")
