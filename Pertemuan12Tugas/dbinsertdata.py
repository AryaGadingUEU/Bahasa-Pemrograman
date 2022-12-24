import mysql.connector

mydb = mysql.connector.connect(
  host="172.30.216.31",
  port=23306,
  user="root",
  password="p455w0rd",
  database="PO_PT_LINTANG_SUMATERA"
)

db = mydb.cursor()

# Insert into Supplier
sql = "INSERT INTO Supplier (kode_supplier, nama_supplier, telepon) VALUES (%s, %s, %s)"
val = [("S120", "PT. Global Jaya Solusi", "0218888777"), ("S210", "PT. Revanda Jaya", "0216567787")]
db.executemany(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert ke tabel Supplier")

# Insert into Pemesan
sql = "INSERT INTO Pemesan (nik, nama_pemesan, email) VALUES (%s, %s, %s)"
val = [("K16001", "Rini Hapsari", "rini@lintangjaya.com"), ("K16007", "Bagas Chandradewa", "bagas@lintangjaya.com")]
db.executemany(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert ke tabel Pemesan")

# Insert into Kategori
sql = "INSERT INTO Kategori(id_kategori, nama_kategori) VALUES (%s, %s)"
val = [("Kt001", "ATK"), ("Kt010", "Elektronik"), ("Kt011", "Inventaris Kantor")]
db.executemany(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert ke tabel Kategori")

# Insert into Barang
sql = "INSERT INTO Barang(id_barang, nama_barang, id_kategori, harga) VALUES (%s, %s, %s, %s)"
val = [("B001", "Pulpen", "Kt001", 15000), ("B002", "Bolpen", "Kt001", 20000), ("B003", "Spidol", "Kt001", 10000), ("B004", "Laptop", "Kt010", 12000000), ("B005", "Monitor", "Kt010", 8000000)]
db.executemany(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert ke tabel Barang")

# Insert into Pesanan
sql = "INSERT INTO Pesanan(no_pesanan, nik, id_barang, jumlah, total) VALUES (%s, %s, %s, %s, %s)"
val = [("P001", "K16001", "B001", 5, 75000), ("P002", "K16007", "B002", 10, 200000), ("P003", "K16007", "B004", 1, 12000000)]
db.executemany(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert ke tabel Pesanan")
