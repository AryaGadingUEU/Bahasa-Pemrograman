import mysql.connector

mydb = mysql.connector.connect(
  host="172.19.164.13",
  port=23306,
  user="root",
  password="",
)

db = mydb.cursor()
db.execute("CREATE DATABASE PO_PT_LINTANG_SUMATERA")