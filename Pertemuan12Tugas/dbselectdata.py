import mysql.connector

mydb = mysql.connector.connect(
  host="172.30.216.31",
  port=23306,
  user="root",
  password="p455w0rd",
  database="PO_PT_LINTANG_SUMATERA"
)

db = mydb.cursor()

# SELECT Supplier
db.execute("SELECT * FROM Supplier")

res = db.fetchall()

print("Tabel Supplier:")

for x in res:
  print(x)

# SELECT Pemesan
db.execute("SELECT * FROM Pemesan")

res = db.fetchall()

print("Tabel Pemesan:")

for x in res:
  print(x)

# SELECT Kategori
db.execute("SELECT * FROM Kategori")

res = db.fetchall()

print("Tabel Kategori:")

for x in res:
  print(x)

# SELECT Barang
db.execute("SELECT * FROM Barang")

res = db.fetchall()

print("Tabel Barang:")

for x in res:
  print(x)

# SELECT Pesanan
db.execute("SELECT * FROM Pesanan")

res = db.fetchall()

print("Tabel Pesanan:")

for x in res:
  print(x)
