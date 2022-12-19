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