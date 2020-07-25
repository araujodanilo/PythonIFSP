buscar = {}
matrizCarros = [["Modelo", "Ano", "ValorCompra", "ValorVenda"],
                ["Gol", 1998, 8000.0, 9500.0],
                ["Fusca", 1978, 5000.0, 6000.0],
                ["Belina", 1981, 4000.0, 6000.0],
                ["Celta", 1997, 6500.0, 7800.0],
                ["Astra", 2005, 14000.0, 15500.0]]
qtdCarros = 6

for i in range(1, qtdCarros):
    buscar[matrizCarros[i][0]] = [matrizCarros[i][1], matrizCarros[i][2], matrizCarros[i][3]]

def Menu():
    print("1 - Cadastro")
    print("2 - Listar modelos")
    print("3 - Buscar modelo")
    print("4 - Informar preço meio das compras")
    print("5 - Modelo mais barato")
    print("6 - Lucro de cada carro")
    print("7 - Lucro obitido do ultimo")

opcao = -1
while opcao != 0:
    Menu()
    opcao = int(input("Digite a opcão: "))
    if opcao == 1:
        cadastro = []
        modelo = input("Digite modelo do carro: ").capitalize()
        cadastro.append(modelo)
        ano = int(input("Digite o ano do carro: "))
        cadastro.append(ano)
        valorCompra = float(input("Digite o valor compra: "))
        cadastro.append(valorCompra)
        valorVenda = float(input("Digite o valor venda: "))
        cadastro.append(valorVenda)
        matrizCarros.append(cadastro)
        qtdCarros += 1
        buscar[modelo] = [ano] + [valorCompra] + [valorVenda]
    elif opcao == 2:
        for i in range(1, qtdCarros):
            print("Modelo: " + matrizCarros[i][0])
    elif opcao == 3:
        somaMediaCompra = 0
        qtdsomaMediaCompra = 0
        for i in range(1, qtdCarros):
            somaMediaCompra += matrizCarros[i][2]
            qtdsomaMediaCompra += 1
        print("Preço médio de compras: " + str(somaMediaCompra/qtdsomaMediaCompra))
    elif opcao == 4:
        chave = input("Digite o modelo do carro: ").capitalize()
        print("Modelo: " + chave + "\nAno: " + str(buscar[chave][0]) + "\nValor Compra: " + str(buscar[chave][1]) + "\nValor Venda: " + str(buscar[chave][2]))
    elif opcao == 5:
        # Esse valor é para venda!!!! -------->>>> para mudar para o de compra só mudar o 3 para 2
        menorValor = matrizCarros[1][3]
        menorValorModelo = matrizCarros[1][0]
        for i in range(2, qtdCarros):
            if menorValor > matrizCarros[i][3]:
                menorValor = matrizCarros[i][3]
                menorValorModelo = matrizCarros[i][0]
        # no codigo tem dois veiculo com menor valor igual mas fiz só aparecer um
        print("Modelo de menor valor: " + menorValorModelo + " Valor: " + str(menorValor))
    elif opcao == 6:
        for i in range(1, qtdCarros):
            print("Modelo: " + matrizCarros[i][0] + "\tLucro: " + str(matrizCarros[i][3]-matrizCarros[i][2]))
    elif opcao == 7:
        menorAno = matrizCarros[1][1]
        menorAnoModelo = matrizCarros[1][0]
        for i in range (2, qtdCarros):
            if menorAno > matrizCarros[i][1]:
                menorAno = matrizCarros[i][1]
                menorAnoModelo = matrizCarros[i][0]
        print("Modelo: " + menorAnoModelo + "\tLucro: " + str(buscar[menorAnoModelo][2]-buscar[menorAnoModelo][1]))
