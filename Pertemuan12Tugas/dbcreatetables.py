import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.188",
  port=23306,
  user="root",
  password="p455w0rd",
  database="PO_PT_LINTANG_SUMATERA"
)
db = mydb.cursor()

db.execute("CREATE TABLE Supplier (kode_supplier char(4) NOT NULL, nama_supplier varchar(22) NOT NULL, telepon char(10) NOT NULL, PRIMARY KEY (kode_supplier))engine=innodb")
db.execute("CREATE TABLE Pemesan (nik char(6) NOT NULL, nama_pemesan varchar(17) NOT NULL, email varchar(21) NOT NULL, PRIMARY KEY (nik))engine=innodb")
db.execute("CREATE TABLE Kategori (id_kategori char(5) NOT NULL, nama_kategori varchar(17) NOT NULL, PRIMARY KEY (id_kategori))engine=innodb")
db.execute("CREATE TABLE Barang (id_barang char(7) NOT NULL, nama_barang varchar(14) NOT NULL, id_kategori char(5) NOT NULL, harga int(7) NOT NULL, PRIMARY KEY (id_barang))engine=innodb")
db.execute("CREATE TABLE Pesanan (no_pesanan char(7) NOT NULL, nik char(6) NOT NULL, id_barang char(7) NOT NULL, jumlah int(5) NOT NULL, total int(7) NOT NULL, PRIMARY KEY (no_pesanan), FOREIGN KEY (nik) REFERENCES Pemesan(nik), FOREIGN KEY (id_barang) REFERENCES Barang(id_barang))engine=innodb")