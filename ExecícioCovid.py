import os

#Se True, vai pular a primeira linha. Se False, não vai pular nehuma
carregarLinha = True
arquivo = "COVID-19-geographic-disbtribution-worldwide.csv"
quebraLinha = ";"
# ------------------------------------------------------------------

class dadosCovid():
    def __init__(self):
        self.data = ""
        self.casos = ""
        self.mortes = ""
        self.pais = ""
        self.populacao = ""
        self.continente = ""

if not os.path.exists(arquivo):
    print("Arquivo não encontado!")

listaDados = []

def CarregarAquivo():
    dadosArquivos = open(arquivo, "r")
    for linhaDados in dadosArquivos:
        linha = linhaDados.split(quebraLinha)
        covid = dadosCovid()
        covid.data = linha[0]
        covid.casos = linha[4]
        covid.mortes = linha[5]
        covid.pais = linha[6].capitalize()
        covid.populacao = linha[9]
        covid.continente = linha[10]
        listaDados.append(covid)
    if carregarLinha:
        del listaDados[0]
    dadosArquivos.close()

def CriarMenu():
    print("Menu:")
    print("1 - Listar pais em uma data")
    print("2 - Informar maior numero de mortes numa data")
    print("3 - Informar menor numero de mortes numa data")
    print("4 - Dados mais recentes de mortes por milhão na europa")
    print("5 - Gerar arquivo informações de morte, população casos de cada continente")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        opcao = -1
    return opcao

def ListarDados():
    pais = input("Digite o pais: ").capitalize()
    data = input("Digite uma data: ")
    if VerificarData(data):
        for dados in listaDados:
            if dados.data == data and dados.pais == pais:
                print("Pais: " + dados.pais + "\tPopulação: " + dados.populacao + "\tCasos: " + dados.casos + "\tMortes: " + dados.mortes + "a: " + dados.continente)
    else:
        print("Data inválida")

def VerificarData(data):
    if len(data) == 10 and data[2] == "/" == data[5]:
        return True
    return False

def ListarMaisMortes():
    data = input("Digite a data: ")
    if VerificarData(data):
        numMortes = int(input("Digite a quantidade: "))
        loop = 0
        for dados in listaDados:
            if int(dados.mortes) >= int(numMortes) and str(dados.data) == data:
                loop += 1
                print("#" + str(loop))
                print("Pais: " + dados.pais + "\tMortes: " + str(dados.mortes))
        if loop == 0:
            print("Não foi encontrado!")
    else:
        print("Data inválida: ")

def ListarMenosMortes():
    data = input("Digite uma data: ")
    if VerificarData(data):
        listaMenosMortes = []
        menorNumero = listaDados[0].mortes
        menorNumeroPais = listaDados[0].pais
        existeMais = False
        for dados in listaDados:
            if data == dados.data:
                if str(menorNumero) > str(dados.mortes):
                    menorNumero = dados.mortes
                    menorNumeroPais = dados.mortes
                    existeMais = False
                elif str(menorNumero) == str(dados.mortes):
                    listaMenosMortes.append(dados)
                    existeMais = True

    if existeMais:
        loop = 0
        for dados in listaMenosMortes:
            loop += 1
            print("#" + str(loop))
            print("Pais: " + dados.pais + "\tMortes: " + str(dados.mortes))
    else:
        print("Pais: " + menorNumeroPais + "\tMortes: " + str(menorNumero))

def SalvarDados():
    continente = input("Digite o continente: ").capitalize()
    somaMortes = 0
    somaPopulacao = 0
    for dados in listaDados:
        if dados.continente == continente:
            somaMortes += int(dados.mortes)
            somaPopulacao += int(dados.populacao)
    if somaPopulacao != 0:
        if not os.path.exists("ArquivoRelatório.txt"):
            dadosArquivo = open("ArquivoRelatório.txt", "w")
            linha = "Continente,Mortes,População\n"
            dadosArquivo.write(linha)
        else:
            dadosArquivo = open("ArquivoRelatório.txt", "a")
        linha = continente + "," + str(somaMortes) + "," + str(somaPopulacao) + "\n"
        dadosArquivo.write(linha)
        dadosArquivo.close()
        print("Arquivo salvo!")
    else:
        print("Não foi possivel")

CarregarAquivo()
opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        ListarDados()
    elif opcao == 2:
        ListarMaisMortes()
    elif opcao == 3:
        ListarMenosMortes()
    elif opcao == 5:
        SalvarDados()
