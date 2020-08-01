class Cliente():
    def __init__(self):
        self.nome = ""
        self.telefone = ""

class Lavagem:
    def __init__(self):
        self.nome = ""
        self.data = ""
        self.modelo = ""
        self.valor = 0.0

listaClientes = []
listaLavagens = []
dadosClientesCarregados = False
dadosLavagensCarregados = False
buscarMes = {}

for indice in range(1, 12):
    if len(str(indice)) == 1:
        indice = "0"+str(indice)
    buscarMes[str(indice)] = 0

def CriarMenu():
    print("Menu:")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadstrar lavagens")
    print("4 - Listar lavagens")
    print("5 - Listar lavagens por mes")
    print("6 - Atualizar dados clientes")
    print("7 - Excluir clientes")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        opcao = -1
        return opcao
    return opcao

def VerificarCliente(nome):
    for cliente in listaClientes:
        if nome == cliente.nome:
            return True
    return False

def CadastrarCliente(nome):
    if VerificarCliente(nome) == False:
        try:
            c = Cliente()
            c.nome = nome
            c.telefone = int(input("Digite o telefone: "))
            listaClientes.append(c)
            print("Cliente cadastrado!")
            return
        except ValueError:
            print("Não foi possivel!")
            return
    else:
        print("Cliente já cadastrado")

def ListarClientes():
    for cliente in listaClientes:
        print("Nome: " + cliente.nome + "\tTelefone: " + str(cliente.telefone))

def CadastrarLavagens():
    nome = input("Digite nome do cliente: ").capitalize()
    if VerificarCliente(nome) == False:
        CadastrarCliente(nome)
    data = input("Digite a data: ")
    if VerificarData(data):
        lavagem = Lavagem()
        lavagem.nome = nome
        lavagem.data = data
        lavagem.modelo = input("Digite o modelo do carro: ").capitalize()
        lavagem.valor = float(input("Digite o valor: "))
        listaLavagens.append(lavagem)
        soma = float(buscarMes[lavagem.data[3:5]]) + float(lavagem.valor)
        buscarMes[lavagem.data[3:5]] += soma
        print("Cadastro concluido!")
    else:
        print("Data inválida!")
        print("Tente novamente  >>> 01/08/2020")

def VerificarData(data):
    if len(data) == 10 and data[2] == "/" == data[5]:
        if int(data[6:]) == 2020 and int(data[3:5]) >= 8 or int(data[6:]) > 2020:
            return True
    return False

def ListarLavagens():
    loop = 0
    for lavagem in listaLavagens:
        loop += 1
        print("#" + str(loop))
        print("Nome: " + lavagem.nome + "\tData:" + lavagem.data)
        print("Modelo:" + lavagem.modelo + "\tValor: " + str(lavagem.valor))

def ListarLavagemMes():
    mes = input("Digite numero do mes: ")
    if len(mes) == 1:
        mes = "0"+str(mes[0])
    print(buscarMes[mes])

def AtualizarDados():
    nome = input("Digite o nome do cliente: ").capitalize()
    if VerificarCliente(nome):
        for lavagem in listaLavagens:
            if lavagem.nome == nome:
                modelo = input("Digite o modelo do carro: ").capitalize()
                if modelo == lavagem.modelo:
                    data = input("Digite a data: ")
                    if VerificarData(data):
                        lavagem.data = data
                        break
                    else:
                        print("Data inválida!")
                        return
        for cliente in listaClientes:
            if cliente.nome == nome:
                cliente.telefone = input("Digite o telefone: ")
                print("Concluido!")
                return
        else:
            print("Não encontrado")
            return
    print("Não foi possivel")

def DeletarCliente():
    print("Exclusão de cliente!!")
    nome = input("Digite o nome do cliente: ").capitalize()
    if VerificarCliente(nome):
        loop = 0
        for cliente in listaClientes:
            if cliente.nome == nome:
                del listaClientes[loop]
                break
            loop += 1
        loop = 0
        for lavagem in listaLavagens:
            if lavagem.nome == nome:
                del listaLavagens[loop]
                print("Apagado!")
                return
            loop += 1
    else:
        print("Não encotrado!")

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        nome = input("Digite o nome: ").capitalize()
        CadastrarCliente(nome)
    elif opcao == 2:
        ListarClientes()
    elif opcao == 3:
        CadastrarLavagens()
    elif opcao == 4:
        ListarLavagens()
    elif opcao == 5:
        ListarLavagemMes()
    elif opcao == 6:
        AtualizarDados()
    elif opcao == 7:
        DeletarCliente()

