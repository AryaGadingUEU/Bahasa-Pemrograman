class Plant(super):
    def __init__(self, statusTumbuh, jumlahAir, jumlahPupuk):
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0
    
    def getJumlahAir(self):
        return self.jumlahAir
    
    def setJumlahAir(self, n):
        self.jumlahAir = n
    
    def getJumlahPupuk(self):
        return self.jumlahPupuk
    
    def setJumlahPupuk(self, n):
        self.jumlahPupuk = n
    
    def setStatusTumbuh(self, n):
        self.statusTumbuh = n

    def beriAir(self):
        self.jumlahAir += 1
        Plant.cekKondisiTumbuh()
    
    def beriPupuk(self):
        self.jumlahPupuk += 1
        Plant.cekKondisiTumbuh()
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=1):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 1
            self.statusTumbuh += 1
    
    def displayPlant(self):
        print(self.getStatusTumbuhText())
        print(f"Jumlah Air: ".format(self.jumlahAir))
        print(f"Jumlah Pupuk: ".format(self.jumlahPupuk))
    
    def getStatusTumbuhText(self):
        if self.statusTumbuh == 0:
            print(f"Status Tanaman: BENIH")
        elif self.statusTumbuh == 1:
            print(f"Status Tanaman: TUNAS")
        elif self.statusTumbuh == 2:
            print(f"Status Tanaman: TANAMAN KECIL")
        elif self.statusTumbuh == 3:
            print(f"Status Tanaman: TANAMAN DEWASA")
        else:
            print(f"Status Tanaman: BERBUNGA")
    
    def getStatusTumbuh(self):
        return self.statusTumbuh
    
    def getImagePath(self):
        self.tImagePath = "A"
        if self.statusTumbuh == 0:
            self.tImagePath = "A"
        elif self.statusTumbuh == 1:
            self.tImagePath = "B"
        elif self.statusTumbuh == 2:
            self.tImagePath = "C"
        elif self.statusTumbuh == 3:
            self.tImagePath = "D"
        elif self.statusTumbuh == 4:
            self.tImagePath = "E"
        
        return self.tImagePath

class Anggrek(Plant):
    def __init__(self, jenis, JumlahAir, JumlahPupuk, statusTumbuh):
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
        self.__jenis = jenis
        print("Jenis Tanaman: {}".format(jenis))
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=2):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 2
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

class Mawar(Plant):
    def __init__(self, jenis, JumlahAir, JumlahPupuk, statusTumbuh):
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
        self.__jenis = jenis
        print("Jenis Tanaman: {}".format(jenis))
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=3):
            Mawar.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 3
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

class Melati(Plant):
    def __init__(self, jenis, JumlahAir, JumlahPupuk, statusTumbuh):
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
        self.__jenis = jenis
        print("Jenis Tanaman: {}".format(jenis))
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=4):
            Melati.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 4
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

# ================ Waktunya Eksekusi! =============================
aAnggrek = Anggrek('Anggrek', 3, 2, 2)
aAnggrek.getStatusTumbuhText()
aAnggrek.displayPlant()

bMawar = Mawar('Mawar', 3, 3, 3)
bMawar.getStatusTumbuhText()
bMawar.displayPlant()

cMelati = Melati('Melati', 3, 4, 4)
cMelati.getStatusTumbuhText()
cMelati.displayPlant()
