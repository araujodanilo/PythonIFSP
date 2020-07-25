m = 8
n = 8

matriz = []
mLoop = 1
for i in range(m):
    linha = []
    nLoop = 1
    for j in range(n):
        if (mLoop%2 != 0 and nLoop%2 == 0) or (mLoop%2 == 0 and nLoop%2 != 0):
            linha.append(1)
        else:
            linha.append(0)
        nLoop += 1
    matriz.append(linha)
    mLoop += 1

for i in range(m):
    print(matriz[i])