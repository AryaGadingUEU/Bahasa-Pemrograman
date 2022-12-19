# Ini adalah bentuk kelas Plant yang telah dikembangkan 
# (Referensi: Modul sesi 6 dan modul sesi 9)

class Plant(super):
    def __init__(self, JumlahWater, JumlahFertilizer, StatusGrown):
        self.JumlahWater = JumlahWater
        self.JumlahFertilizer = JumlahFertilizer
        self.StatusGrown = StatusGrown

    def grown(self):
        if self.StatusGrown < 4:
            self.JumlahWater -= 3
            self.JumlahFertilizer -= 1
            self.StatusGrown += 1
    
    def getJumlahWater(self):
        return self.JumlahWater
    
    def setJumlahWater(self, x):
        self.JumlahWater = x
    
    def getJumlahFertilizer(self):
        return self.JumlahFertilizer
    
    def setJumlahFertilizer(self, x):
        self.JumlahFertilizer = x 
    
    def setStatusGrown(self, x):
        self.StatusGrown = x
    
    def beriWater(self):
        self.JumlahWater += 1
        Plant.cekKondisiGrown()
    
    def beriFertilizer(self):
        self.JumlahFertilizer += 1
        Plant.cekKondisiGrown()
    
    def cekKondisiGrown(self):
        if self.JumlahWater >= 3 and self.JumlahFertilizer >= 1:
            Plant.grown()

    def displayPlant(self):
        print("Jumlah Air: {} \nJumlah Pupuk: {}".format(self.JumlahWater, self.JumlahFertilizer))

    def getStatusGrownText(self):
        if self.StatusGrown == 0:
            print("Status Tanaman: BENIH") 
        elif self.StatusGrown == 1:
            print("Status Tanaman: TUNAS")
        elif self.StatusGrown == 2:
            print("Status Tanaman: TANAMAN KECIL")
        elif self.StatusGrown == 3:
            print("Status Tanaman: TANAMAN DEWASA")
        elif self.StatusGrown == 4:
            print("Status Tanaman: BERBUNGA")
        else:
            print("Status Tanaman: UNKNOWN")
    
    def getStatusGrown(self):
        return self.StatusGrown

# Dari kelas utama / superclass Plant, dibuatlah kelas turunan.
# Kelas turunan yang dimaksud adalah Anggrek, Mawar, Melati
# Setiap kelas memiliki karakteristik khusus yang berbeda-beda yang bisa saya asumsikan sendiri disini.

class Anggrek(Plant):
    def __init__(self, JumlahWater, JumlahFertilizer, StatusGrown, jenis):
        self.jenis = jenis
        Plant.__init__(self, JumlahWater, JumlahFertilizer, StatusGrown)
    
    def anggrek_grown(self):
        if self.StatusGrown < 4:
            self.JumlahWater -= 3
            self.JumlahFertilizer -= 2
            self.StatusGrown += 1
    
    def cekKondisiGrown(self):
        if self.JumlahWater >= 3 and self.JumlahFertilizer >= 2:
            Anggrek.anggrek_grown()
    
    def getjenis(self):
        return self.jenis

class Mawar(Plant):
    def __init__(self, JumlahWater, JumlahFertilizer, StatusGrown, jenis):
        self.jenis = jenis
        Plant.__init__(self, JumlahWater, JumlahFertilizer, StatusGrown)
    
    def mawar_grown(self):
        if self.StatusGrown < 4:
            self.JumlahWater -= 3
            self.JumlahFertilizer -= 3
            self.StatusGrown += 1
    
    def cekKondisiGrown(self):
        if self.JumlahWater >= 3 and self.JumlahFertilizer >= 3:
            Mawar.mawar_grown()
    
    def getjenis(self):
        return self.jenis

class Melati(Plant):

    def __init__(self, JumlahWater, JumlahFertilizer, StatusGrown, jenis):
        self.jenis = jenis
        Plant.__init__(self, JumlahWater, JumlahFertilizer, StatusGrown)
    
    def melati_grown(self):
        if self.StatusGrown < 4:
            self.JumlahWater -= 3
            self.JumlahFertilizer -= 4
            self.StatusGrown += 1
    
    def cekKondisiGrown(self):
        if self.JumlahWater >= 3 and self.JumlahFertilizer >= 4:
            Melati.melati_grown()
    
    def getjenis(self):
        return self.jenis

# ================ Waktunya Eksekusi! =============================

Tanaman1 = Anggrek(3, 2, 2, 'Anggrek')
print("Jenis Tanaman: {}".format(Tanaman1.jenis))
Tanaman1.getStatusGrownText()
Tanaman1.displayPlant()

Tanaman2 = Mawar(3, 3, 3, 'Mawar')
print("\nJenis Tanaman: {}".format(Tanaman2.jenis))
Tanaman2.getStatusGrownText()
Tanaman2.displayPlant()

Tanaman3 = Melati(3, 4, 4, 'Melati')
print("\nJenis Tanaman: {}".format(Tanaman3.jenis))
Tanaman3.getStatusGrownText()
Tanaman3.displayPlant()

