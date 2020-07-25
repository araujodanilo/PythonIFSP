m = 8
n = 8

matriz = []

mloop=1
for i in range(m):
    linha=[]
    nloop = 1
    for j in range(n):
        if mloop == 2 and nloop == 7:
            linha.append(8)
        elif nloop == mloop:
            linha.append(2)
        elif nloop > mloop:
            linha.append(0)
        else:
            linha.append(1)
        nloop +=1
    mloop += 1
    matriz.append(linha)

for i in range(m):
    print(matriz[i])