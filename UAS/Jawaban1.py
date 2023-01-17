class Bunga:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def tampilkan_nama(self):
        print(f"Nama bunga: {self.nama}")

    def tampilkan_warna(self):
        print(f"Warna bunga: {self.warna}")

class Mawar(Bunga):
    def __init__(self,nama,warna,bentuk):
        super().__init__(nama, warna)
        self.bentuk = bentuk
    def tampilkan_bentuk(self):
        print(f"Bentuk bunga Mawar: {self.bentuk}\n")

class Melati(Bunga):
    def __init__(self,nama,warna,bau):
        super().__init__(nama, warna)
        self.bau = bau
    def tampilkan_bau(self):
        print(f"Bau bunga Melati: {self.bau}\n")

class Anggrek(Bunga):
    def __init__(self, nama, warna, ukuran):
        super().__init__(nama, warna)
        self.ukuran = ukuran
    def tampilkan_ukuran(self):
        print(f"Ukuran bunga Anggrek: {self.ukuran}\n")

mawar = Mawar("Mawar Merah", "Merah", "Bulat")
mawar.tampilkan_nama()
mawar.tampilkan_warna()
mawar.tampilkan_bentuk()

melati = Melati("Melati Putih", "Putih", "Wangi")
melati.tampilkan_nama()
melati.tampilkan_warna()
melati.tampilkan_bau()

anggrek = Anggrek("Anggrek Merah", "Merah", "Besar")
anggrek.tampilkan_nama()
anggrek.tampilkan_warna()
anggrek.tampilkan_ukuran()
