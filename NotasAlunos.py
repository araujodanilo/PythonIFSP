tamanho = 5# Português, Matemática, Física, Geografia, História

""" Só é possivel ver a materia se for escrito corretamente """

matrizNotas = ["", "Português", "Matemática", "Física", "Geografia", "História"]

matrizNotas = [["", "p", "m", "f", "g", "h"],
               ["Danilo", 7.0, 10.0, 6.0, 8.0, 9.0],
               ["Danilo2", 4.0, 2.0, 7.0, 0.0, 9.0],
               ["Danilo3", 5.0, 8.0, 0.0, 0.0, 5.0],
               ["Danilo4", 8.0, 9.0, 2.0, 3.0, 4.0]]
                                                    #"""

def Menu():
    print("1 - Cadastar")
    print("2 - Ver notas do aluno:")
    print("3 - Média da disciplina")
    print("4 - Aluno maior nota de matematica")
    print("5 - Média do Aluno")
    print("6 - Menor nota, informar disciplina e aluno")

def VerAluno(nome):
    for linha in matrizNotas:
        if linha[0].lower() == nome.lower():
            print("Português: " + str(linha[1]))
            print("Matemática: " + str(linha[2]))
            print("Física: " + str(linha[3]))
            print("Geografia: " + str(linha[4]))
            print("História: " + str(linha[5]))

def CalcularMediaDisciplina(disciplina):
    nloop = 0
    okay = False
    for i in range(tamanho):
        for j in matrizNotas[i]:
            if j.lower() == disciplina.lower():
                okay = True
                break
            nloop += 1
        if okay == True:
            break
    soma = 0
    divisor = 0
    okay = False
    for valor in [j[nloop] for j in matrizNotas]:
        if okay == True:
            soma += valor
            divisor += 1
        else:
            okay = True
    if divisor > 0:
        print("Média da disciplina: " + str(soma/divisor))
    else:
        print("Não foi possivel!")

def MaiorNotaMatematica():
    maiorNota = 0
    contador = 0
    okay = False
    for valor in [j[2] for j in matrizNotas]:
        if okay == True:
            if maiorNota < valor:
                maiorNota = valor
                maiorNotaNome = [j[0] for j in matrizNotas][contador]
        else:
            okay = True
        contador += 1
    print("Nome do aluno: " + maiorNotaNome + " Nota: " + str(maiorNota))

def CalcularMediaAlunos():
    primeiraLinha = False
    loop = 0
    for i in range(tamanho):
        soma = 0
        okay = False
        if primeiraLinha == False:
            primeiraLinha = True
        else:
            for j in matrizNotas[i]:
                if okay == False:
                    okay = True
                else:
                    soma += j
            print("Nome do aluno: " + [j[0] for j in matrizNotas][loop] + " Média: " + str(soma/5))
        loop += 1

def MenorNota():
    menorNota = 11
    contadorLinha = 0
    primeiraLinha = False
    menorNotaNome = ""
    menorNotaDisciplina = ""
    for linha in matrizNotas:
        okay = False
        contadorColuna = 0
        if primeiraLinha == False:
            primeiraLinha = True
        else:
            for coluna in linha:
                if okay == False:
                    okay = True
                else:
                    if menorNota > coluna:
                        menorNota = coluna
                        menorNotaNome = str(matrizNotas[contadorLinha][0])
                        menorNotaDisciplina = matrizNotas[0][contadorColuna]
                contadorColuna += 1
        contadorLinha += 1
    print("Nome do aluno: " + menorNotaNome)
    print("Nome da Disciplina: " + menorNotaDisciplina)
opcao = -1
while opcao != 0:
    Menu()
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        nome = input("Nome do aluno: ")
        nPort = float(input("Nota Português: "))
        nMat = float(input("Nota Matemática: "))
        nFis = float(input("Nota Física: "))
        nGeo = float(input("Nota Geografia: "))
        nHis = float(input("Nota História: "))
        coluna = [str(nome)] + [str(nPort)] + [str(nMat)] + [str(nFis)] + [str(nGeo)] + [str(nHis)]
        matrizNotas.append(coluna)
    elif opcao == 2:
        nome = input("Digite nome do aluno: ")
        VerAluno(nome)
    elif opcao == 3:
        materia = input("Digite nome da disciplina: ")
        CalcularMediaDisciplina(materia)
    elif opcao == 4:
        MaiorNotaMatematica()
    elif opcao == 5:
        CalcularMediaAlunos()
    elif opcao == 6:
        MenorNota()

