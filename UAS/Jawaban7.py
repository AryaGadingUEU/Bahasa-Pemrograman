import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.188",
  port=23306,
  user="root",
  password="p455w0rd",
  database="PO_PT_Rakhasa_Jaya"
)
db = mydb.cursor()

db.execute("CREATE TABLE Supplier (kode_supplier char(4) NOT NULL, nama_supplier varchar(22) NOT NULL, telepon char(10) NOT NULL, PRIMARY KEY (kode_supplier))engine=innodb")

sql = "INSERT INTO Supplier (kode_supplier, nama_supplier, telepon) VALUES (%s, %s, %s)"
val = [("S120", "PT. Global Jaya Solusi", "0218888777"), ("S210", "PT. Revanda Jaya", "0216567787")]
db.executemany(sql, val)
mydb.commit()

db.execute("SHOW DATABASES")
for x in db:
  print(x)

