matrizCanil = []

qtdCachorros = 0 # a contagem de cachorros cadastrados

class Cachorro:
    def __init__(self):
        self.nome = ""
        self.peso = 0.0
        self.raca = ""
        self.idade = 0

#Opcões menu
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
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print('\nOpção inválida!')
        print("")
        ret = -1
    return opcao

# Defini aqui a varivel pois como vou usar a varivel para ser usada em outra função e é preciso denifir como global
# Tem que definir antes também
indice = 0

# Aqui a verifica se  cao foi casdastrado
def ExisteCao(nome):
    global indice # Definindo a variavel para global pois o python  aparece um erro no compilador
    existe = False
    for indice in range(qtdCachorros):
        if nome == matrizCanil[indice][0].lower():
            existe = True
    return existe, indice

# Aqui é para cadastrar o cao e já salvar na matriz
def CadastroDog():
    global qtdCachorros # Definindo a variavel para global pois o python  aparece um erro no compilador
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
        qtdCachorros += 1
        print("Cadastrado!")
    else:
        print("Nome cão ja existe!")

# Dado um nome de um cachorro  atualiza o dados dele
def AtualizarDados(nome):
    existe, indice = ExisteCao(nome)
    if existe == True:
        matrizCanil[indice][1] = float(input("Digite novo peso: "))
        matrizCanil[indice][2] = input("Qual raça do cao: ")
        matrizCanil[indice][3] = int(input("Nova idade do dog: "))
        print("Dados Atualizados")
    else:
        print("Não encontrado!")

# Função para achar o cachrro com maior idade
def VerCachorrosMaisVelho():
    maiorIdade = 0
    nomeMaiorIdade = ""
    for indice in range(qtdCachorros):
        if matrizCanil[indice][3] > maiorIdade:
            maiorIdade = matrizCanil[indice][3]
            nomeMaiorIdade = matrizCanil[indice][0]
    print("Nome do dog mais velho: " + str(nomeMaiorIdade) + "\tIdade: " + str(maiorIdade))

# De todos cacchros cadastrados ele apaga todos que sãoo da raça pitbull
def ExcluirPitbull():
    global qtdCachorros # Definindo a variavel para global pois o python  aparece um erro no compilador
    for indice in range(qtdCachorros):
        if (matrizCanil[indice][2]).lower() == "pitbull":
            del matrizCanil[indice]
            qtdCachorros = qtdCachorros - 1

# Calcula o percentual de vira-latas cadastrados
def VerPercentualViraLata():
    qtdCachorrosViraLata = 0
    for indice in range(qtdCachorros):
        if (matrizCanil[indice][2]).lower() == "vira-lata" or (matrizCanil[indice][2]).lower() == "viralata":
            qtdCachorrosViraLata += 1
    if qtdCachorros !=0:
        print("Pecentual de vira-latas: " + str(qtdCachorrosViraLata*100/qtdCachorros) + "%")
    else:
        print("Erro!")

# Acha o cachorro com menor peso
def VerCachorroMenorPeso():
    menorPesoDog = matrizCanil[0][1]
    menorPesoDogNome = matrizCanil[0][0]
    for indice in range(1, qtdCachorros):
        if matrizCanil[indice][1] < menorPesoDog:
            menorPesoDog = matrizCanil[indice][1]
            menorPesoDogNome = matrizCanil[indice][0]
    print("Nome dog: " + menorPesoDogNome + "\tPeso: " + str(menorPesoDog))

# Conta todos tipos de raça e exibi todas elas
def VerQuantidadesdeRacas():
    global qtdCachorros # Definindo a variavel para global pois o python  aparece um erro no compilador
    racaContagem = {}
    racaNome = []
    for indice in range(qtdCachorros):
        existe = False
        for racas in racaContagem:
            if matrizCanil[indice][2].lower() == racas:
                existe = True
                racaContagem[matrizCanil[indice][2]] += 1
                break
        if existe == False:
            racaContagem[matrizCanil[indice][2]] = 1
            racaNome.append(matrizCanil[indice][2])
    for racas in racaNome:
        print("Raça: " + racas + "\tQuantidade: " + str(racaContagem[racas]))

# Faz uma contagem de 2kg de ração por cada kilo de peso dos cachorros
def VerificarEstoque():
    somaPeso = 0
    for indice in range(qtdCachorros):
        somaPeso +=matrizCanil[indice][1]
    if somaPeso > 0:
        print("Quantidade necessária para proximos 12 meses: " + str((somaPeso*2/qtdCachorros)*12) + "kg")
    else:
        print("Erro!")

opcao = -1
while opcao != 0:
    opcao = VerMenu()
    if opcao == 1:
        CadastroDog()
    elif opcao == 2:
        nome = input("Digite nome do dog: ").lower()
        AtualizarDados(nome)
    elif opcao == 3:
        VerCachorrosMaisVelho()
    elif opcao == 4:
        ExcluirPitbull()
    elif opcao == 5:
        VerPercentualViraLata()
    elif opcao == 6:
        VerCachorroMenorPeso()
    elif opcao == 7:
        VerQuantidadesdeRacas()
    elif opcao == 8:
        VerificarEstoque()
