import os

class Paciente():
    def __init__(self):
        self.nome = ""
        self.nomeMedico = ""
        self.valor = 0.0
        self.data = ""

class Medico():
    def __init__(self):
        self.nome = ""
        self.especilidade = ""
        self.valor = 0.0

listaPacientes = []
listaMedicos = []

arquivoPacientes = "pacientes.txt"
if not os.path.exists(arquivoPacientes):
    print("Arquivo não encontado!")

def CriarMenu():
    print("Menu:")
    print("1 - Carregar lista paciente")
    print("2 - Listar pacientes")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Opção inválida!")
        opcao = -1
    return opcao

def CarregarPacientes():
    arquivo = open(arquivoPacientes, "r")
    for dados in arquivo:
        linha = dados.split(",")
        p = Paciente()
        p.nome = linha[1]
        listaPacientes.append(p)
    del listaPacientes[0]
    arquivo.close()

def ListarPacientes():
    loop = 0
    for paciente in listaPacientes:
        loop += 1
        print("#" + str(loop))
        print("Nome: " + paciente.nome + "\tNome do médico: " + paciente.nomeMedico)
        print("Data: " + paciente.data + "\tValor: " + str(paciente.valor))
opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        CarregarPacientes()
    elif opcao == 2:
        ListarPacientes()