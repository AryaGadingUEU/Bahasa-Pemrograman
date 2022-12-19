# UTS PEMROGRAMAN BERBASIS OBJEK EU301

Dalam Ujian Tengah Semester kali ini, ada 5 soal yang diujikan dalam pelajaran Pemrograman Berbasis Objek (EU301). Diantaranya adalah:

- Jelaskan narasi singkat tentang paradigma Pemrograman dan apakah yang dimaksud dengan pemograman berorientasi objek?
- Buatlah program seperti dibawah ini sesuaikan dengan nim dan nama anda
    ```
    =================
    Quiz
    ====================
    masukkan nama   : <namamu>
    masukkan nim    : <nimmu>
    ```

- Jelaskan perbedaan looping dengan continue dan break dari codingan di bawah ini
```
for val in "bahasa":
    if val == "h":
        continue
        #break
    print (val)
print ("selesai")
```

- Buat program pembelanjaan (Capucino, Teh, dan Exit) dengan menggunakan PPN 10%!
- Buatlah dengan class dan definition terkait inputan jam, menit, detik yang dimana jam hanya bisa 24, menit 60, detik 60!

## Jawaban Nomor 1
-  Paradigma pemrograman bisa dikatakan sebagai sebuah teknik menggolongkan bahasa pemrograman atas fitur-fitur yang dipunya. Makna lain dari paradigma ialah teknik-teknik berbeda dalam menulis sebuah program guna jadi berbagai penyelesaian banyak masalah. Paradigma pemrograman sendiri bisa digolongkan lebih lanjut menjadi 4, yakni procedural programming, functional programming, object-oriented programming, dan logical programming.
-  Pemrograman berorientasi objek adalah paradigma pemrograman yang didasarkan atas konsep “objek” yang berisi data, atau bentuk bidang/atribut. Fitur pemrograman berorientasi objek sendiri ada enkapsulasi, inheritance, polymorphism, data abstraction.

## Jawaban Nomor 2
Kodingannya adalah:
```
def utama():
    print("=================")
    print("PROGRAM QUIZ")
    print("====================")

utama()

def display():
    input("masukkan nama : ") #masukkan nama : Arya Gading
    int(input("masukkan nim : ")) #masukkan nim : 20210801321

display()
```

Hasil outputnya adalah:
```
=================
PROGRAM QUIZ
====================
masukkan nama : Arya Gading
masukkan nim : 20210801321
```

## Jawaban Nomor 3
Kodingan (break) adalah:
```
for val in "bahasa":
    if val == "h":
        break
    print(val)
print("selesai")

#Dari segi looping, perbedaan antara continue dan break ialah
#Kalau kodingan kita menggunakan continue, maka perulangan akan diulang terus
#sampai sampai akhir dan variabel “h” akan dilangkahi / dilewati
#Sedangkan kalau kodingan kita menggunakan “break”, maka perulangan akan dihentikan seketika
#perulangannya telah mencapi “h” dan tidak diteruskan lagi perulangannya sejak “h”.
```

atau
kodingan (continue) adalah:
```
for val in "bahasa":
    if val == "h":
        continue
    print(val)
print("selesai")

#Dari segi looping, perbedaan antara continue dan break ialah
#Kalau kodingan kita menggunakan continue, maka perulangan akan diulang terus
#sampai sampai akhir dan variabel “h” akan dilangkahi / dilewati
#Sedangkan kalau kodingan kita menggunakan “break”, maka perulangan akan dihentikan seketika
#perulangannya telah mencapi “h” dan tidak diteruskan lagi perulangannya sejak “h”.
```

Output (break) adalah:
```
b
a
selesai
```

Output (continue) adalah:
```
b
a
a
s
a
selesai
```

Kesimpulannya adalah:
Dari segi looping, perbedaan antara continue dan break adalah
Kalau kodingan kita menggunakan continue, maka perulangan akan diulang terus sampai sampai akhir dan variabel “h” akan dilangkahi / dilewati. 
Sedangkan kalau kodingan kita menggunakan “break”, maka perulangan akan dihentikan seketika perulangannya telah mencapi “h” dan tidak diteruskan lagi perulangannya sejak “h”.


## Jawaban Nomor 4
Kodingannya adalah:
```
def info():
    int(input("NIM : ")) #NIM: 20210801321
    input("NAMA : ") #NAMA: Arya Gading

info()

def pilih():
    opsi="y"
    while opsi=="y":
        print("\nPilihan")
        print("1. capucino")
        print("2. teh")
        print("3. Exit")
        pil=int(input("masukkan pilihan : "))
        
        if pil==1:
            print("memilih CAPUCINO")
            cpc=int(input("masukkan harga : "))
            print(cpc+(cpc*0.1))
            
            opsi=input("Apakah masih mau melanjutkan pemesanannya [y/n]? ")
            
        elif pil==2:
            print("memilih TEH")
            teh=int(input("masukkan harga : "))
            print(teh+(teh*0.1))

            opsi=input("Apakah masih mau melanjutkan pemesanannya [y/n]? ")
        
        elif pil==3:
            print("\nTerima kasih telah berbelanja di tempat kami!")
            break
        
        else:
            print("Nomor pilihan yang anda masukkan salah! Silahkan dicoba lagi!")
    
    while opsi=="n":
        print("\nTerima kasih telah berbelanja di tempat kami!")
        break
pilih()
```

Hasil outputnya adalah:
```
NIM : 20210801321
NAMA : Arya Gading

Pilihan
1. capucino
2. teh
3. Exit
masukkan pilihan : 1
memilih CAPUCINO
masukkan harga : 3000
3300.0
Apakah masih mau melanjutkan pemesanannya [y/n]? y

Pilihan
1. capucino
2. teh
3. Exit
masukkan pilihan : 3

Terima kasih telah berbelanja di tempat kami!
```

## Jawaban Nomor 5
Kodingannya adalah:
```
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
```

Hasil outputnya adalah:
```
masukkan jam: 23
masukkan menit: 56
masukkan detik: 56
23 : 56 : 56
```

# Structure Folder UTS
```
📦UTS
 ┣ 📜Jawaban1.py
 ┣ 📜Jawaban2.py
 ┣ 📜Jawaban3.py
 ┣ 📜Jawaban4.py
 ┗ 📜Jawaban5.py
 ┗ 📜Readme.MD
```
## Credit
> Arya Gading (NIM: 20210801321)