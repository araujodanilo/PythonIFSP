class Animal():
    def __init__(self):
        self.nome = ""
        self.raca = ""
        self.idade = 0

listaAnimais = []

def CriarMenu():
    print("Menu: ")
    print("1 - Cadastrar animal")
    print("Listar")
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        opcao = -1
        print("Opção inválida!")
    return opcao

def VerificarNome(nome, lista):
    for elemento in lista:
        if elemento.nome == nome:
            return True
    return False

def CadastrarAnimal():
    a = Animal()
    a.nome = input("Digite o nome: ").capitalize()
    if VerificarNome(a.nome, listaAnimais) == False:
        a.raca = input("Digite a raça: ").capitalize()
        a.idade = int(input("Digite a idade: "))
        listaAnimais.append(a)
    else:
        print("Já existe!")

def ListarAnimais():
    print("Lista animais:")
    for animal in listaAnimais:
        print("Nome: " + animal.nome + "\tRaça: " + animal.raca + "\tIdade: " + str(animal.idade))

opcao = -1
while opcao != 0:
    opcao = CriarMenu()
    if opcao == 1:
        CadastrarAnimal()
    elif opcao == 2:
        ListarAnimais()