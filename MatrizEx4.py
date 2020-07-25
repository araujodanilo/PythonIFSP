m = 8
n = 8

matriz = []

cont = -2
mLoop = 1
for i in range(m):
    linha = []
    nLoop = 1
    if mLoop%2 != 0:
        cont += 2
    for j in range(n):
        if nLoop == 1:
            cont= cont
        elif mLoop%2 == 0:
            cont -= 1
        else:
            cont += 1
        linha.append(cont)
        nLoop += 1
    mLoop += 1
    matriz.append(linha)

for i in range(m):
    print(matriz[i])