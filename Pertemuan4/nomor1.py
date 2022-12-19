from datetime import date

TahunSekarang = date.today().year
TahunLahir=int(input("Masukkan Tahun Lahir Kamu: "))
usia=int(TahunSekarang-TahunLahir)

print("\nKamu lahir di tahun",TahunLahir,".")
print("Sekarang sudah tahun",TahunSekarang,".")
print("\nKini, usiamu ialah",usia,"tahun.")