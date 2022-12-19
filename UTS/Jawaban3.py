for val in "bahasa":
    if val == "h":
        continue
        #break
    print(val)
print("selesai")

#Dari segi looping, perbedaan antara continue dan break ialah
#Kalau kodingan kita menggunakan continue, maka perulangan akan diulang terus
#sampai sampai akhir dan variabel “h” akan dilangkahi / dilewati
#Sedangkan kalau kodingan kita menggunakan “break”, maka perulangan akan dihentikan seketika
#perulangannya telah mencapi “h” dan tidak diteruskan lagi perulangannya sejak “h”.