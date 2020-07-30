class Cliente():
    def __init__(self):
        self.nome = ""
        self.telefone = 0

class Lavagem():
    def __init__(self):
        self.clinte = ""
        self.modelo = ""
        self.data = ""
        self.valor = 0.0


matrizCliente = []
matrizLavagem = []
buscarCliente = {}
varivelCadastados = 0
varivelLavagens = 0
buscarLucro = {}
indice = 0

def CriarMenu():
    print("Menu:")
    print("1 - Cadastar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar lavagem")
    print("4 - Listar lavgens")
    print("5 - Faturamento esitmado")
    print("6 - Atualizar lavagem")
    print("7 - Excluir cliente")
    try:
        opcao = int(input("Digite a opcao: "))
    except ValueError:
        print("Opção inválida")
        opcao = -1
    return opcao

def ExisteNome(nome, contagemLista):
    global indice
    existe = False
    for indice in range(contagemLista):
        if matrizCliente[indice][0].lower() == nome:
            existe = True
    return existe, indice

def Cadastrar(nome):
    global varivelCadastados
    existe, indice = ExisteNome(nome, varivelCadastados)
    if existe == False:
        CadastroCliente = []
        c = Cliente()
        c.nome = nome
        try:
            c.telefone = int(input("Digite o telefone: "))
        except ValueError:
            print("Telefone inválido!")
            return False
        CadastroCliente.append(c.nome)
        CadastroCliente.append(c.telefone)
        buscarCliente[c.nome] = c.telefone
        matrizCliente.append(CadastroCliente)
        varivelCadastados += 1
        return True
    else:
        print("Nome já existente!")
        return False

def ListarClientes():
    print("Cadastados:")
    for indice in range(varivelCadastados):
        print("Nome :" + matrizCliente[indice][0] + "\tTelefone: " + str(matrizCliente[indice][1]))

def CadastrarLavagem(cliente):
    global varivelLavagens
    existe, indice = ExisteNome(cliente, varivelCadastados)
    if existe == False:
        existe = Cadastrar(cliente)
        if existe == False:
            return
    data = input("Digite a data: ")
    correto = VerificarData(data)
    if correto:
        lavagem = Lavagem()
        lavagem.clinte = cliente
        lavagem.data = data
        lavagem.modelo = input("Digite o modelo do carro: ")
        lavagem.valor = float(input("Digite o valor da lavagem: "))
        varivelLavagens += 1
        buscarLucro[data[3:8]] = lavagem.valor
        print("Cadastro lavagem feita!")
    else:
        print("Data inválida")
        return

def ListarLavagem(mes):
    listarLavagens = []
    for indice in range(varivelLavagens):
        data = str(matrizLavagem[indice][2])
        if data[3:5] == mes:
            listarLavagens.append(matrizLavagem[indice])
    for lavagem in listarLavagens:
        print("Cliente: " + lavagem[0] + "\tVeiculo: " + lavagem[1] + "\nValor: " + lavagem[3] + "\tData: " + lavagem[2])

def LucroEstimadoMes():
    for indice in range(1, 12):
        print(buscarLucro[indice])

def VerificarData(data):
    if data[2] == "/" == data[5] and len(data) == 10:
        if int(data[6:]) == 2020 and int(data[3:5]) >= 8 or int(data[6:]) > 2020:
            return True
    return False

def AtualizarLavagem():
    nome = input("Digite nome do cliente: ")
    existe = ExcluirCliente(nome)
    if existe == False:
        print("Cliente não existe!")
        return
    modelo = input("Digite modelo do carro do cliente: ")
    for indice in range(varivelLavagens):

    for indice in range(varivelLavagens):
        if matrizLavagem[indice][0].lower() == cliente.lower() and matrizLavagem[indice][1].lower() == modelo.lower():
            while True:
                data = input("Digite a data: ")
                correto = VerificarData(data)
                if correto:
                    break
                else:
                    print("Data inválida!")

def ExcluirCliente(cliente):
    global varivelLavagens, varivelCadastados
    existeC, indice = ExisteNome(cliente, varivelCadastados)
    if existeC:
        del matrizCliente[indice]
        varivelCadastados -= 1
    existeL, indice = ExisteNome(cliente, varivelLavagens)
    if existeL:
        del matrizLavagem[indice]
        varivelLavagens -= 1

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        nome = input("Digite o nome do cliente: ")
        Cadastrar(nome)
    elif opcao == 2:
        ListarClientes()
    elif opcao == 3:
        nome = input("Digite o nome do cliente: ")
        CadastrarLavagem(nome)
    elif opcao == 4:
        mes = input("Digite o numero do mes: ")
        ListarLavagem(mes)
    elif opcao == 5:
        LucroEstimadoMes()
    elif opcao == 6:
        AtualizarLavagem()
    elif opcao == 7:
        nome = input("Digite nome do cliente: ")
        ExcluirCliente(nome)