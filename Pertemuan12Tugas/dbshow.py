import mysql.connector

mydb = mysql.connector.connect(
  host="172.30.216.31",
  port=23306,
  user="root",
  password="p455w0rd",
)

db = mydb.cursor()
db.execute("SHOW DATABASES")
for x in db:
  print(x)