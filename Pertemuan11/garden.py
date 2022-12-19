<<<<<<< HEAD
# Heading
import tkinter as tk
from tkinter import ttk #Frame Input
from tkinter import *
from tkinter.messagebox import showinfo #Import Display Show Info

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("800x800")
window.resizable(False, False)
window.title("WELCOME TO UGARDEN") #Judul

# Variabel dan Fungsi


# Frame Input
input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen-komponen GUI
teks_atas_label = ttk.Label(input_frame, text="Selamat Datang di Toko Bunga Arya Gading\n".center(160))
teks_atas_label.pack(padx=10,fill="x",expand=True)

# Class Garden dan anak2nya
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
        print("Jumlah Air: ".format(self.jumlahAir))
        print("Jumlah Pupuk: ".format(self.jumlahPupuk))
    
    def getStatusTumbuhText(self):
        if self.statusTumbuh == 0:
            return "Benih"
        elif self.statusTumbuh == 1:
            return "Tunas"
        elif self.statusTumbuh == 2:
            return "Tanaman Kecil"
        elif self.statusTumbuh == 3:
            return "Tanaman Dewasa"
        else:
            return "Berbunga"
    
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
        super()
        self.__jenis = "Anggrek"
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
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
        super()
        self.__jenis = "Mawar"
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=3):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 3
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

class Melati(Plant):
    def __init__(self, jenis, JumlahAir, JumlahPupuk, statusTumbuh):
        super()
        self.__jenis = jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=4):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 4
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

## Anggrek
def click_beriair_1():
    pesan = f"Sukses memberi air pada tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_1():
    pesan = f"Sukses memberi pupuk pada tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

def click_panen_1():
    pesan = f"Sukses memanen tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

anggrek_label = ttk.Label(input_frame, text="-> Bunga Anggrek\n\n\n")
anggrek_label.pack(padx=10,fill="x",expand=True)

tombol_beriair_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_1)
tombol_beriair_label.pack(expand=True,padx=10,pady=10)
tombol_beriair_label.place(x=10, y=65)

tombol_beripupuk_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_1)
tombol_beripupuk_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk_label.place(x=110, y=65)

tombol_panen_label = ttk.Button(input_frame,text="Panen",command=click_panen_1)
tombol_panen_label.pack(expand=True,padx=10,pady=10)
tombol_panen_label.place(x=210, y=65)

## Mawar
def click_beriair_2():
    pesan = f"Sukses memberi air pada tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_2():
    pesan = f"Sukses memberi pupuk pada tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

def click_panen_2():
    pesan = f"Sukses memanen tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

Mawar_label = ttk.Label(input_frame, text="-> Bunga Mawar\n\n\n")
Mawar_label.pack(padx=10,fill="x",expand=True)

tombol_beriair2_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_2)
tombol_beriair2_label.pack(expand=True,padx=10,pady=10)
tombol_beriair2_label.place(x=10, y=135)

tombol_beripupuk2_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_2)
tombol_beripupuk2_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk2_label.place(x=110, y=135)

tombol_panen2_label = ttk.Button(input_frame,text="Panen",command=click_panen_2)
tombol_panen2_label.pack(expand=True,padx=10,pady=10)
tombol_panen2_label.place(x=210, y=135)

## Melati
def click_beriair_3():
    pesan = f"Sukses memberi air pada tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_3():
    pesan = f"Sukses memberi pupuk pada tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

def click_panen_3():
    pesan = f"Sukses memanen tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

Melati_label = ttk.Label(input_frame, text="-> Bunga Melati\n\n\n")
Melati_label.pack(padx=10,fill="x",expand=True)

tombol_beriair3_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_3)
tombol_beriair3_label.pack(expand=True,padx=10,pady=10)
tombol_beriair3_label.place(x=10, y=205)

tombol_beripupuk3_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_3)
tombol_beripupuk3_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk3_label.place(x=110, y=205)

tombol_panen3_label = ttk.Button(input_frame,text="Panen",command=click_panen_3)
tombol_panen3_label.pack(expand=True,padx=10,pady=10)
tombol_panen3_label.place(x=210, y=205)

# Tombol Keluar
def click_keluar():
    pesan = f"Terima kasih telah menggunakan program kami!"
    showinfo(title="HASIL",message=pesan)
    if pesan: window.quit()

tombol_keluar = ttk.Button(input_frame,text="KELUAR",command=click_keluar)
tombol_keluar.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()
=======
# Heading
import tkinter as tk
from tkinter import ttk #Frame Input
from tkinter import *
from tkinter.messagebox import showinfo #Import Display Show Info

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("800x800")
window.resizable(False, False)
window.title("WELCOME TO UGARDEN") #Judul

# Variabel dan Fungsi


# Frame Input
input_frame = ttk.Frame(window)
#Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen-komponen GUI
teks_atas_label = ttk.Label(input_frame, text="Selamat Datang di Toko Bunga Arya Gading\n".center(160))
teks_atas_label.pack(padx=10,fill="x",expand=True)

# Class Garden dan anak2nya
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
        print("Jumlah Air: ".format(self.jumlahAir))
        print("Jumlah Pupuk: ".format(self.jumlahPupuk))
    
    def getStatusTumbuhText(self):
        if self.statusTumbuh == 0:
            return "Benih"
        elif self.statusTumbuh == 1:
            return "Tunas"
        elif self.statusTumbuh == 2:
            return "Tanaman Kecil"
        elif self.statusTumbuh == 3:
            return "Tanaman Dewasa"
        else:
            return "Berbunga"
    
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
        super()
        self.__jenis = "Anggrek"
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
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
        super()
        self.__jenis = "Mawar"
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=3):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 3
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

class Melati(Plant):
    def __init__(self, jenis, JumlahAir, JumlahPupuk, statusTumbuh):
        super()
        self.__jenis = jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, statusTumbuh)
    
    def cekKondisiTumbuh(self):
        if(self.jumlahAir >=3 and self.jumlahPupuk >=4):
            Plant.tumbuh()

    def tumbuh(self):
        if(self.statusTumbuh < 4):
            self.jumlahAir -= 3
            self.jumlahPupuk -= 4
            self.statusTumbuh += 1
    
    def getjenis(self):
        return self.__jenis

## Anggrek
def click_beriair_1():
    pesan = f"Sukses memberi air pada tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_1():
    pesan = f"Sukses memberi pupuk pada tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

def click_panen_1():
    pesan = f"Sukses memanen tanaman Anggrek!"
    showinfo(title="HASIL",message=pesan)

anggrek_label = ttk.Label(input_frame, text="-> Bunga Anggrek\n\n\n")
anggrek_label.pack(padx=10,fill="x",expand=True)

tombol_beriair_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_1)
tombol_beriair_label.pack(expand=True,padx=10,pady=10)
tombol_beriair_label.place(x=10, y=65)

tombol_beripupuk_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_1)
tombol_beripupuk_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk_label.place(x=110, y=65)

tombol_panen_label = ttk.Button(input_frame,text="Panen",command=click_panen_1)
tombol_panen_label.pack(expand=True,padx=10,pady=10)
tombol_panen_label.place(x=210, y=65)

## Mawar
def click_beriair_2():
    pesan = f"Sukses memberi air pada tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_2():
    pesan = f"Sukses memberi pupuk pada tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

def click_panen_2():
    pesan = f"Sukses memanen tanaman Mawar!"
    showinfo(title="HASIL",message=pesan)

Mawar_label = ttk.Label(input_frame, text="-> Bunga Mawar\n\n\n")
Mawar_label.pack(padx=10,fill="x",expand=True)

tombol_beriair2_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_2)
tombol_beriair2_label.pack(expand=True,padx=10,pady=10)
tombol_beriair2_label.place(x=10, y=135)

tombol_beripupuk2_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_2)
tombol_beripupuk2_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk2_label.place(x=110, y=135)

tombol_panen2_label = ttk.Button(input_frame,text="Panen",command=click_panen_2)
tombol_panen2_label.pack(expand=True,padx=10,pady=10)
tombol_panen2_label.place(x=210, y=135)

## Melati
def click_beriair_3():
    pesan = f"Sukses memberi air pada tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

def click_beripupuk_3():
    pesan = f"Sukses memberi pupuk pada tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

def click_panen_3():
    pesan = f"Sukses memanen tanaman Melati!"
    showinfo(title="HASIL",message=pesan)

Melati_label = ttk.Label(input_frame, text="-> Bunga Melati\n\n\n")
Melati_label.pack(padx=10,fill="x",expand=True)

tombol_beriair3_label = ttk.Button(input_frame,text="Beri Air",command=click_beriair_3)
tombol_beriair3_label.pack(expand=True,padx=10,pady=10)
tombol_beriair3_label.place(x=10, y=205)

tombol_beripupuk3_label = ttk.Button(input_frame,text="Beri Pupuk",command=click_beripupuk_3)
tombol_beripupuk3_label.pack(expand=True,padx=10,pady=10)
tombol_beripupuk3_label.place(x=110, y=205)

tombol_panen3_label = ttk.Button(input_frame,text="Panen",command=click_panen_3)
tombol_panen3_label.pack(expand=True,padx=10,pady=10)
tombol_panen3_label.place(x=210, y=205)

# Tombol Keluar
def click_keluar():
    pesan = f"Terima kasih telah menggunakan program kami!"
    showinfo(title="HASIL",message=pesan)
    if pesan: window.quit()

tombol_keluar = ttk.Button(input_frame,text="KELUAR",command=click_keluar)
tombol_keluar.pack(fill='x',expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()
>>>>>>> 4960e2cbf496aaa0f36c18dd1aedbef2fd55728c
