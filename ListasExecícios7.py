def Menu():
    print("1 - Inserir elementos na Lista 1")
    print("2 - Inserir elementos na Lista 2")
    print("3 - Exibir conteúdos das duas listas")
    print("4 - Lista que junta as duas (ListaUniao)")
    print("5 - Lista intersecção")
    print("6 - Somar todos valor da primeira lista e somar com maior")
    print("7 - Multiplicar valores das duas listas")
    print("8 - Zerar as duas listas")
    print("9 - Ordenar ListaUniao decrescente")

lista1 = []
lista2 = []
opcaoQuatro = False

def InserirListaDois(elemento):
    loop = 0
    opcaoQuatro = False
    while loop != 5:
        lista2.append(elemento)
        elemento *= 2
        loop += 1

def PrintLista(lista):
    for elemento in lista:
        print(elemento)

opcao = -1
while opcao != 0:
    Menu()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        lista1 = []
        loop = 0
        while loop != 5:
            elemento = int(input("Digite valor do elemento " + str(loop+1) + ": "))
            lista1.append(elemento)
            loop += 1
            opcaoQuatro = False
    if opcao == 2:
        elemento = int(input("Digite valor do elemento: "))
        InserirListaDois(elemento)
    if opcao == 3:
        print("Lista #1")
        PrintLista(lista1)
        print("Lista #2")
        PrintLista(lista2)
    if opcao == 4:
        ListaUniao = []
        for elemento in lista1:
            ListaUniao.append(elemento)
        for elemento in lista2:
            ListaUniao.append(elemento)
        print("ListaUniao: ")
        PrintLista(ListaUniao)
        opcaoQuatro = True
    if opcao == 5:
        LI = []
        for numeroListaUm in lista1:
            for numeroListaDois in lista2:
                if numeroListaUm == numeroListaDois:
                    LI.append(numeroListaDois)
        print("Lista intersecção:")
        PrintLista(LI)
    if opcao == 6:
        maiorNumero = 0
        soma = 0
        for elemento in lista2:
            if maiorNumero < elemento:
                maiorNumero = elemento
        for elemento in lista1:
            if maiorNumero < elemento:
                maiorNumero = elemento
            soma += elemento
        soma += maiorNumero
        print("Soma: " + str(soma))
    if opcao == 7:
        LM = []
        loop = 0
        while loop != 5:
            elemento =  lista2[loop] * lista1[loop]
            LM.append(elemento)
            loop += 1
        print("Lista Multiplicada:")
        PrintLista(LM)
    if opcao == 8:
        lista1 = []
        lista2 = []
        opcaoQuatro = False
    if opcao == 9:
        if opcaoQuatro == True:
            ListaUniao.sort(reverse=True)
            print(ListaUniao)
            PrintLista(ListaUniao)
        else:
            print("Primeiro use a opção 4!")
