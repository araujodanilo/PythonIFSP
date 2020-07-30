import os

cursosLista = []
alunosLista = []
carregado = False

def VerificarExiste(curso):
    for elemento in cursosLista:
        if curso == elemento:
            return True
    return False

def CadastrarCursos(curso):
    existe = VerificarExiste(curso)
    if existe == False:
        cursosLista.append(curso)
        print("Curso cadastrado com sucesso")
    else:
        print("Erro curso já existente")

def ListarCursos():
    print("Cursos:")
    for cursos in cursosLista:
        print(cursos)

def CadastrarAluno():
    curso = input("Nome do curso: ")
    existe = VerificarExiste(curso)
    if existe:
        aluno = []
        aluno.append(curso)
        nome = input("Nome do aluno: ")
        aluno.append(nome)
        idade = str(input("Nome do idade: "))
        aluno.append(idade)
        media = float(input("Nome do media: "))
        aluno.append(media)
        alunosLista.append(aluno)
    else:
        print("Curso não existe!")

def ListarAluno():
    for aluno in alunosLista:
        print("Nome: " + aluno[0] + " Curso: " + aluno[1].upper() + " Idade: " + str(aluno[2]) + " Média: " + str(aluno[3]))

def ListarAlunosOrdenados():
    cursosLista.sort()
    for curso in cursosLista:
        print("Curso: " + curso)
        for aluno in alunosLista:
            if curso == aluno[1]:
                print("Nome: " + aluno[0] + " Idade: " + str(aluno[2]) + " Média: " + str(aluno[3]))

def CalcularMediaIdades():
    somaIdadesAluno = 0
    qtdAluno = 0
    for aluno in alunosLista:
        qtdAluno += 1
        somaIdadesAluno += int(aluno[2])
    if qtdAluno != 0 or somaIdadesAluno == 0:
        print("Média das idades: " + str(somaIdadesAluno/qtdAluno))
    else:
        print("Não foi possivel")

def ArquivoADS():
    file = "AlunosADS.txt"
    arquivo = open(file, 'w')
    for aluno in alunosLista:
        if int(aluno[3]) >= 7 and aluno[1].lower() == "ads":
            arquivo.write(aluno[0] + ", " + aluno[1] + ", " + str(aluno[2]) + ", " + str(aluno[3]) + "\n")
    arquivo.close()
    print("Arquivo descarregado!")

def ContarAlunosCursos():
    nomeCurso = ""
    qtdCurso = 0
    for curso in cursosLista:
        qtdAluno = 0
        for aluno in alunosLista:
            if curso.lower() == aluno[1].lower():
                qtdAluno += 1
        if qtdCurso < qtdAluno:
            nomeCurso = curso
            qtdCurso =  qtdAluno
    print("Curso: " + nomeCurso + "\tQuantidade: " + str(qtdCurso))

def CalcularMediaNotasCurso():
    for curso in cursosLista:
        somaNotas = 0
        qtdAlunos = 0
        for aluno in alunosLista:
            if curso.lower() == aluno[1].lower():
                somaNotas += float(aluno[3])
                qtdAlunos += 1
        if qtdAlunos != 0 or somaNotas != 0:
            print("Curso: " + curso + "\tMédia: " + str(somaNotas/qtdAlunos))
        else:
            print("Não foi possivel calcular média do curso: " + curso)

def ColocarNoArquivo():
    file = "Alunos.txt"
    if carregado == True:
        arquivo = open(file, 'w')
    else:
        arquivo = open(file, 'a')
    for aluno in alunosLista:
        arquivo.write(aluno[0] + ", " + aluno[1] + ", " + str(aluno[2]) + ", " + str(aluno[3]) + "\n")
    arquivo.close()
    print("Arquivo descarregado!")

def ImportarDados():
    global carregado
    file = "Alunos.txt"
    if os.path.exists(file):
        arquivo = open(file, 'r')
        arquivo.seek(0)
        for linha in arquivo:
            dados = linha.split(", ")
            aluno = [dados[0]] + [dados[1]] + [int(dados[2])] + [dados[3].replace("\n", "")]
            alunosLista.append(aluno)
            CadastrarCursos(aluno[1])
        arquivo.close()
        carregado = True
        print("Arquivo carregado!")
    else:
        print("Arquivo não exite!")

def CriarMenu():
    print("Menu:")
    print("1 - Cadastar curso")
    print("2 - Listar cursos")
    print("3 - Cadastar aluno")
    print("4 - Listar alunos")
    print("5 - Listar alunos em ordem")
    print("6 - Média de idades aluno")
    print("7 - Criar lista alunos que tem media maior que 7 de ads")
    print("8 - Informar qual curso tem mais alunos")
    print("9 - Informar media do melhor curso")
    print("10 - Exportar arquivos com dados dos alunos")
    print("11 - Importar dados dos alunos")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Error")
        opcao = -1
    return opcao

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        curso = input("Digite nome do curso: ")
        CadastrarCursos(curso)
    elif opcao == 2:
        ListarCursos()
    elif opcao == 3:
        CadastrarAluno()
    elif opcao == 4:
        ListarAluno()
    elif opcao == 5:
        ListarAlunosOrdenados()
    elif opcao == 6:
        CalcularMediaIdades()
    elif opcao == 7:
        ArquivoADS()
    elif opcao == 8:
        ContarAlunosCursos()
    elif opcao == 9:
        CalcularMediaNotasCurso()
    elif opcao == 10:
        ColocarNoArquivo()
    elif opcao == 11:
        ImportarDados()



