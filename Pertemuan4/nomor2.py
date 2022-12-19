print("===================================")
print("Stand Kentang Goreng - Arya Gading")
print("===================================")
pembeli = input("Masukkan nama Pembeli: ")

def listkentang():
   global totalporsi1
   global porsi
   global kentang
   print ("\n----------------- List Kentang Goreng -----------------")
   print("1. Kentang Goreng Biasa - Rp 24000")
   print("2. Kentang Goreng Tipis - Rp 19000")
   print("3. Kentang Goreng Keriting - Rp 28000")
   pil=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if pil==1:
       totalporsi1=porsi*24000
       print (porsi," porsi Kentang Goreng Biasa = Rp", totalporsi1)
       kentang=("Kentang Goreng Biasa")
   elif pil==2:
       totalporsi1=porsi*19000
       print (porsi," porsi Kentang Goreng Tipis = Rp", totalporsi1)
       kentang=("Kentang Goreng Tipis")
   elif pil==3:
       totalporsi1=porsi*28000
       print (porsi, " porsi Kentang Goreng Keriting = Rp", totalporsi1)
       kentang=("Kentang Goreng Keriting")
   else:
      print("Pilihan tidak ada, mohon untuk memilih pilihannya dengan benar!")
      listkentang()

def listsaus():
   global totalporsi2
   global porsi2
   global saus
   print("\n----------------- List Saus Kentang Goreng -----------------")
   print("1. BBQ - Rp 6000")
   print("2. Rumput Laut - Rp 5000")
   print("3. Keju - Rp 4000")
   pil=int(input("Masukan Pilihan: "))
   porsi2= int(input("Berapa Porsi: "))

   if pil==1:
       totalporsi2=porsi2*6000
       print (porsi2," BBQ = Rp", totalporsi2)
       saus=("BBQ")
   elif pil==2:
       totalporsi2=porsi2*5000
       print (porsi2, " Rumput Laut = Rp", totalporsi2)
       saus=("Rumput Laut")
   elif pil==3:
       totalporsi2=porsi2*4000
       print (porsi2, " Keju = Rp", totalporsi2)
       saus=("Keju")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      listsaus()

listkentang()
listsaus()
totalnoppn=totalporsi1+totalporsi2
totalppn=(totalporsi1+totalporsi2)*0.1
totalsemua=((totalporsi1+totalporsi2)*0.1)+(totalporsi1+totalporsi2)

print("\nTotal awal: Rp",totalnoppn)
print("Total PPN (10%): Rp",totalppn)
print("Total yang harus dibayar + PPN: Rp",totalsemua)
uang=int(input("\nUang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian : Rp",kembalian)

print("\n===================================")
print("          STRUK   PEMBELIAN")
print("===================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,kentang,"( Rp", totalporsi1,")")
print ("Dengan Saus\t:",porsi2,saus,"( Rp", totalporsi2,")")
print ("Tagihan Awal\t\t\t: Rp",totalnoppn)
print ("Tagihan PPN (10%)\t\t: Rp", totalppn)
print ("Tagihan + PPN (10%)\t\t: Rp", totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")