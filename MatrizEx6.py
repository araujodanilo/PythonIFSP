m = 8
n = 8

matriz = []
matrizT = []

mloop= 1
for i in range(m):
    nloop=1
    linha= []
    for j in range(n):
        if mloop == nloop:
            linha.append(0)
        elif mloop+nloop == 9:
            linha.append(8)
        elif mloop > nloop and nloop+mloop < 9 \
                or mloop < nloop and nloop+mloop < 9:
            linha.append(1)
        else:
            linha.append(2)
        nloop += 1
    matriz.append(linha)
    mloop += 1

for i in range(m):
    print(matriz[i])

for l in range(5):
    print("")

nloop= 1
for j in range(n):
    coluna = []
    mloop = 1
    for i in range(m):
        if mloop == nloop:
            coluna.append(0)
        elif nloop + mloop == 9:
            coluna.append(8)
        elif nloop > mloop and mloop + nloop < 9 \
                or nloop < mloop and mloop + nloop < 9:
            coluna.append(1)
        else:
            coluna.append(2)
        mloop += 1
    matrizT.append(coluna)
    nloop += 1

for i in range(m):
    print(matrizT[i])