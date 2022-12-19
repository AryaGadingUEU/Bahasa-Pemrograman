print("Penjumlahan Matriks 2x2")

matrix1 = [
    [5, 0],
    [2, 6],
]

matrix2 = [
    [1, 0],
    [4, 2],
]

for x in range(0, len(matrix1)):
    for y in range(0, len(matrix1[0])):
        print(matrix1[x][y] + matrix2[x][y], end=' ')
    print('')
