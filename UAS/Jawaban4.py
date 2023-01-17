def bagi(x, y):
    try:
        hasil = x / y
    except ZeroDivisionError:
        hasil = "Error: Tidak bisa dibagi dengan nol!"
    return hasil

print(bagi(10,2))
print(bagi(10,0))

