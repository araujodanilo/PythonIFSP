class Aluno():
    def __init__(self):
        self.nome = ""
        self.notaProva = 0.0
        self.notaTrabalho = 0.0
        self.frequencia = 0.0
        self.media = 0.0

listaAlunos = []
opcao3Executada = False


def Menu():
    print("Menu")
    print("1- Cadastrar")
    print("2- Listar Alunos")
    print("3- Calcular média")
    print("4- Informar do aluno...")
    print("5- Criar lista com aluno com mais de 8 de média")
    print("5- ver sitações dos alunos")

def CadastrarAluno():
    a = Aluno()
    a.nome = input("Digite nome do Aluno: ")
    a.notaProva = float(input("Digite nota da prova: "))
    a.notaTrabalho = float(input("Digite nota da trabalho: "))
    a.frequencia = float(input("Digite a frequencia do aluno: "))
    listaAlunos.append(a)

def ListarAlunos():
    loop = 0
    for aluno in listaAlunos:
        print("#" + str(loop))
        print(aluno.nome)
        print(aluno.notaProva)
        print(aluno.notaTrabalho)
        print(aluno.frequencia)
        if opcao3Executada:
            print(aluno.media)
        loop += 1

def CalcularMedia():
    opcao3Executada = True
    for aluno in listaAlunos:
        aluno.media = aluno.notaProva*0.7 + aluno.notaTrabalho*0.3

def VerMedia(nome):
    if opcao3Executada:
        for aluno in listaAlunos:
            if aluno.nome.lower() == nome.lower():
                print("Nome: " + aluno.nome + " Média " + str(aluno.media))
    else:
        print("Média não calculada, use opcao 3 primeiro")


def AlunosMaisOito():
    if opcao3Executada:
        listaAlunosMaisOito = []
        for aluno in listaAlunos:
            if aluno.media >= 8:
                listaAlunosMaisOito.append(aluno)
    else:
        print("Primeiro use a opção 3.")

def VerificarSituacao():
    for aluno in listaAlunos:
        if aluno.media >= 6 and aluno.frequencia >= 75:
            print("Aluno: " + aluno.nome)
            print("Aprovado")
        if 4 <= aluno.media < 6 and aluno.frequencia >= 75:
            print("Aluno: " + aluno.nome)
            print("IFA")
        if aluno.media < 4 or aluno.frequencia < 75:
            print("Aluno: " + aluno.nome)
            print("Reprovado")

opcao = -1
while opcao != 0:
    Menu()
    opcao = int(input("Digite a opcao desejada: "))
    if opcao == 1:
        CadastrarAluno()
    elif opcao == 2:
        ListarAlunos()
    elif opcao == 3:
        CalcularMedia()
    elif opcao == 4:
        nome = input("Digite nome do Aluno: ")
        VerMedia(nome)
    elif opcao == 5:
        AlunosMaisOito()
    elif opcao == 6:
        VerificarSituacao()