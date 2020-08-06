import os

class Agendamento():
    def __init__(self):
        self.nome = ""
        self.nomeMedico = ""
        self.valor = ""
        self.data = ""

class Paciente():
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.status = ""

class Medico():
    def __init__(self):
        self.nome = ""
        self.especilidade = ""
        self.valor = 0.0

listaPacientes = []
listaMedicos = []
listaAgendamentos = []

arquivoPacientes = "pacientes.txt"
if not os.path.exists(arquivoPacientes):
    print("Arquivo não encontado!")

def CriarMenu():
    print("Menu:")
    print("1 - Carregar lista paciente")
    print("2 - Listar pacientes")
    print("3 - Cadastrar médico")
    print("4 - Listar medicos")
    print("5 - Agendar consulta")
    print("6 - Listar consultas")
    print("7 - Listar consultas de cardiologista")
    print("8 - Gerar arquivo das consultas")
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
        p.nome = linha[1].capitalize()
        p.idade = linha[2]
        p.status = linha[3].replace("\n", "")
        listaPacientes.append(p)
    del listaPacientes[0]
    arquivo.close()

def ListarPacientes():
    loop = 0
    for paciente in listaPacientes:
        loop += 1
        print("#" + str(loop))
        print("Nome: " + paciente.nome + "\tIdade: " + str(paciente.idade))
        if paciente.status:
            v = "Ativo"
        else:
            v = "Inativo"
        print("Status: " + v)

def CadastrarMedico():
    m = Medico()
    m.nome = input("Digite o nome do medico: ").capitalize()
    if VerificarNome(m.nome, listaMedicos) :
        m.especilidade = input("Digite a especialidade: ").capitalize()
        m.valor = float(input("Digite o valor: "))
        listaMedicos.append(m)
    else:
        print("Médico já existe!")

def ListarMedicos():
    loop =0
    for medico in listaMedicos:
        loop += 1
        print("#" + str(loop))
        print("Nome: " + medico.nome + "\tEspecialidade: " + medico.especilidade)
        print("Valor: " + str(medico.valor))

def VerificarNome(nome, lista):
    for elemento in lista:
        if elemento.nome == nome:
            return True
    return False

def VerificarStatus(nome):
    for elemento in listaPacientes:
        if nome == elemento.nome:
            if elemento.status[0] == "T":
                return True
    return False

def VericarData(data):
    if len(data) == 10 and data[2] == "/" == data[5]:
        if data[0:2] < 32 and data[3:5] < 13:
            return True
    return False

def AgendarConsulta():
    a = Agendamento()
    a.nome = input("Digite o nome do paciente: ").capitalize()
    if VerificarStatus(a.nome):
        a.nomeMedico = input("Digite o nome do medico: ").capitalize()
        if VerificarNome(a.nomeMedico, listaMedicos):
            a.data = input("Digite a data: ")
            if VericarData(a.data):
                a.valor = float(input("Digite o valor: "))
                listaAgendamentos.append(a)
            else:
                print("Data inválida!")
        else:
            print("Medico não listado!")
    else:
        print("Paciente não listado/inativo!")

def ListarAgendamentos():
    loop = 0
    for a in listaAgendamentos:
        loop += 1
        print("#" + str(loop))
        print("Nome paciente: " + a.nome + "\tNome médico: " + a.nomeMedico)
        print("Data: " + a.data + "\tValor: " + str(a.valor))

def ListarCardiologista():
    loop = 0
    listaMedicosCardio = []
    for medico in listaMedicos:
        if medico.especilidade == "Cardiologista":
            listaMedicosCardio.append(medico.nome)
    for agendamento in listaAgendamentos:
        for medico in listaMedicosCardio:
            if medico == agendamento.nomeMedico:
                loop += 1
                print("#" + str(loop))
                print("Nome paciente: " + agendamento.nome + "\tNome médico: " + agendamento.nomeMedico)
                print("Data: " + agendamento.data + "\tValor: " + str(agendamento.valor))

def gerarAquivoConsutas():
    arquivoNome = "Consultas.txt"
    arquivo = open(arquivoNome, "a")
    for dados in listaAgendamentos:
        linha = dados.nome + "," + dados.nomeMedico + "," + dados.data + "," + str(dados.valor) + "\n"
        arquivo.write(linha)
    arquivo.close()

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        CarregarPacientes()
    elif opcao == 2:
        ListarPacientes()
    elif opcao == 3:
        CadastrarMedico()
    elif opcao == 4:
        ListarMedicos()
    elif opcao == 5:
        AgendarConsulta()
    elif opcao == 6:
        ListarAgendamentos()
    elif opcao == 7:
        ListarCardiologista()
    elif opcao == 8:
        gerarAquivoConsutas()