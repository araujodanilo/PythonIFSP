import os

def VereficarArquivos(nomeArquivo):
    if os.path.exists(nomeArquivo):
        return True
    return False

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
    print("3 - Salvar dados clientes")
    print("4 - Carregar dados clientes")
    print("5 - Cadstrar lavagens")
    print("6 - Listar lavagens")
    print("7 - Salvar dados lavagens")#XLS
    print("8 - Carregar dados lavagens")
    print("9 - Listar lavagens por mes")
    print("10 - Criar relatório de lucro por mes")
    print("11 - Atualizar dados clientes")
    print("12 - Excluir clientes")
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

def SalvarDadosClientes():
    if dadosClientesCarregados:
        dadosClientes = open("DadosClientes.xls", "w")
    else:
        dadosClientes = open("DadosClientes.xls", "a")
    for cliente in listaClientes:
        linha = str(cliente.nome) + "," + str(cliente.telefone) + "\n"
        dadosClientes.write(linha)
    dadosClientes.close()

def CarregarDadosClientes():
    if VereficarArquivos("DadosClientes.xls"):
        dadosClientes = open("DadosClientes.xls", "r")
        for dados in dadosClientes:
            linha = dados.split(",")
            c = Cliente()
            c.nome = linha[0].capitalize()
            if VerificarCliente(c.nome) == False:
                c.telefone = linha[1].replace("\n", "")
                listaClientes.append(c)
        dadosClientes.close()
        return True
    else:
        print("Arquivo não existe")
        return False

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

def SalvarDadosLavagens():
    if dadosLavagensCarregados:
        dadosLavagem = open("DadosLavagens.xls", "w")
    else:
        dadosLavagem = open("DadosLavagens.xls", "a")
    for lavagem in listaLavagens:
        linha = lavagem.nome+ ","+lavagem.data+","+lavagem.modelo+","+str(lavagem.valor)+"\n"
        dadosLavagem.write(linha)
    dadosLavagem.close()

def CarregarDadosLavagens():
    if VereficarArquivos("DadosLavagens.xls"):
        dadosLavagem = open("DadosLavagens.xls", "r")
        for dados in dadosLavagem:
            linha = dados.split(",")
            lavagem = Lavagem()
            lavagem.nome = linha[0].capitalize()
            if VerificarCliente(lavagem.nome) == False:
                lavagem.data = linha[1]
                lavagem.modelo = linha[2].capitalize()
                lavagem.valor = linha[3].replace("\n", "")
                listaLavagens.append(lavagem)
                soma = float(buscarMes[lavagem.data[3:5]]) + float(lavagem.valor)
                buscarMes[lavagem.data[3:5]] += soma
        dadosLavagem.close()
        return True
    else:
        print("Arquivo não existe")
        return False

def ListarLavagemMes():
    mes = input("Digite numero do mes: ")
    if len(mes) == 1:
        mes = "0"+str(mes[0])
    print(buscarMes[mes])

def CriarRelatorio():
    dadosRelatorio = open("dadosRelatorios.xls", "w")
    for mes in range(1, 12):
        if len(str(mes)) == 1:
            mes = "0"+str(mes)
        linha = str(mes) + "," + str(buscarMes[str(mes)]) + "\n"
        dadosRelatorio.write(linha)
    dadosRelatorio.close()

def AtualizarDados():
    if CarregarDadosLavagens():
        if CarregarDadosClientes():
            nome = input("Digite o nome do cliente: ").capitalize()
            if VerificarCliente(nome):
                for lavagem in listaLavagens:
                    if lavagem.nome == nome:
                        modelo = input("Digite o modelo do carro: ").capitalize()
                        if modelo == lavagem.modelo:
                            data = input("Digite a data: ")
                            if VerificarData(data):
                                lavagem.data = data
                                SalvarDadosLavagens()
                                break
                            else:
                                print("Data inválida!")
                                return
                for cliente in listaClientes:
                    if cliente.nome == nome:
                        cliente.telefone = input("Digite o telefone: ")
                        print("Concluido!")
                        SalvarDadosClientes()
                        return
                else:
                    print("Não encontrado")
                    return
    print("Não foi possivel")

def DeletarCliente():
    print("Exclusão de cliente!!")
    if CarregarDadosLavagens():
        if CarregarDadosClientes():
            nome = input("Digite o nome do cliente: ").capitalize()
            if VerificarCliente(nome):
                loop = 0
                for cliente in listaClientes:
                    if cliente.nome == nome:
                        del listaClientes[loop]
                        SalvarDadosClientes()
                        break
                    loop += 1
                loop = 0
                for lavagem in listaLavagens:
                    if lavagem.nome == nome:
                        del listaLavagens[loop]
                        print("Apagado!")
                        SalvarDadosLavagens()
                        return
                    loop += 1
            else:
                print("Não encotrado!")
    print("Não foi possivel")

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        nome = input("Digite o nome: ").capitalize()
        CadastrarCliente(nome)
    elif opcao == 2:
        ListarClientes()
    elif opcao == 3:
        SalvarDadosClientes()
        print("Dados Salvos!")
    elif opcao == 4:
        CarregarDadosClientes()
        dadosClientesCarregados = True
        print("Dados importados!")
    elif opcao == 5:
        CadastrarLavagens()
    elif opcao == 6:
        ListarLavagens()
    elif opcao == 7:
        SalvarDadosLavagens()
        print("Dados Salvos!")
    elif opcao == 8:
        CarregarDadosLavagens()
        dadosLavagensCarregados = True
        print("Dados importados!")
    elif opcao == 9:
        ListarLavagemMes()
    elif opcao == 10:
        CriarRelatorio()
    elif opcao == 11:
        AtualizarDados()
        dadosClientesCarregados = True
        dadosLavagensCarregados = True
    elif opcao == 12:
        DeletarCliente()
        dadosClientesCarregados = True
        dadosLavagensCarregados = True

