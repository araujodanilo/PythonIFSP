chave = {}
matrizCanil = []

qtdCachorros = 0

class Cachorro:
    def __init__(self):
        self.nome = ""
        self.peso = 0.0
        self.raca = ""
        self.idade = 0

def VerMenu():
    print("Menu")
    print("1 - Cadastro animal")
    print("2 - Atualizar dados cachorro")
    print("3 - Nome do cão mais velho")
    print("4 - Excluir cachorros da raça pitbull")
    print("5 - Percentual de cachorro vila-lata")
    print("6 - Cachorro de menor peso")
    print("7 - Quantidade de cachorros de cada raça")
    print("8 - Estoque nessesário para o canil")

def ExisteCao(nome):
    existe = False
    for indice in range(qtdCachorros):
        if nome == (matrizCanil[indice].nome).lower():
            existe = True
    return existe, indice

def CadastroDog():
    variavelCachorro = []
    c = Cachorro()
    c.nome = input("Digite nome do cão: ").lower()
    existe, indice = ExisteCao(c.nome)
    if existe == False:
        variavelCachorro.append(c.nome)
        c.peso = float(input("Peso do dog: "))
        variavelCachorro.append(c.peso)
        c.raca = input("Qual a raça: ").lower()
        variavelCachorro.append(c.raca)
        c.idade = int(input("Quantos anos o cachorro tem: "))
        variavelCachorro.append(c.idade)
        matrizCanil.append(variavelCachorro)
        chave[c.nome] = [c.peso] + [c.raca] + [c.idade]
        qtdCachorros += 1
        print("Cadastrado!")
    else:
        print("Nome cão ja existe!")

def AtualizarDados(nome):
    existe, indice = ExisteCao(nome)
    if existe == True:
        del chave[nome]
        matrizCanil[indice].peso = float(input("Digite novo peso: "))
        matrizCanil[indice].raca = input("Qual raca do cao: ")
        matrizCanil[indice].idade = int(input("Nova idade do dog: "))
        chave[nome] = [matrizCanil[indice].peso] + [matrizCanil[indice].raca] + [matrizCanil[indice].idade]
        print("Dados Atualizados")
    else:
        print("Não encontrado!")

def CachorrosMaisVelho():
    maiorIdade = 0
    nomeMaiorIdade = ""
    for indice in range(qtdCachorros):
        if matrizCanil[indice].idade > maiorIdade:
            maiorIdade = matrizCanil[indice].idade
            nomeMaiorIdade = matrizCanil[indice].nome
    print("Nome do dog mais velho: " + str(nomeMaiorIdade) + "\tIdade: " + str(maiorIdade))

def ExcluirPitbull():
    for indice in range(1, qtdCachorros):
        if (matrizCanil[indice].raca).lower() == "pitbull":
            del chave[matrizCanil[indice].nome]
            del matrizCanil[indice]
            qtdCachorros = qtdCachorros - 1

def PercentualViraLata():
    qtdCachorrosViraLata = 0
    for indice in range(qtdCachorros):
        if (matrizCanil[indice].raca).lower() == "vira-lata" or (matrizCanil[indice].raca).lower() == "viralata":
            qtdCachorrosViraLata += 1

def CachorroMenorPeso():
    menorPesoDog = matrizCanil[0].peso
    menorPesoDogNome = matrizCanil[0].nome
    for indice in range(1, qtdCachorros):
        if matrizCanil[indice].peso < menorPesoDog:
            menorPesoDog = matrizCanil[indice].peso
            menorPesoDogNome = matrizCanil[indice].nome

def VerQuantidadesdeRacas():
    class RacasDogs():
        def __init__(self):
            self.nome = ""
            self.qtd = 0
    listasRacas = []
    for indice in range(qtdCachorros):
        eiste = False
        for racas in listasRacas:
            if (matrizCanil[indice].nome).lower() == racas:
                racas.qtd += 1
                existe = True
                break
        if existe == False:
            r = RacasDogs()
            r.nome = RacasDogs
            r.qtd = 1
            listasRacas.append(r)
