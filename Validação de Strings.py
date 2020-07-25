from datetime import date

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def DATA(data):
    valido = False
    while True:
        if data[2] == "-" == data[5] or data[2] == "/" == data[5]:
            dia = data[0:2]
            mes = data[3:5]
            ano = data[-4:]
        if ano < str(date.today().year):
            valido = True
            break
        if ano == str(date.today().year):
            print("a")
            if mes.replace("0", "") == str(date.today().month):
                print("b")
                if dia < str(date.today().day):
                    valido = True
                    break
                if dia >= str(date.today().day):
                    print("Data com dia igual ou maior do que a de hoje")
            if mes != "10":
                if mes.replace("0", "") > str(date.today().month):
                    print("Data com mes maior do que a de hoje")
            if mes == "10":
                if mes > str(date.today().month):
                    print("Data com mes maior do que a de hoje")
        if ano > str(date.today().year):
            print("Data com ano igual ou maior do que a de hoje")
        data = input("Digite a data: ")
    if valido == False:
        print("Tente data --> dd/mm/yyyy")
        data = input("Digite a data: ")



def EMAIL(email):
    while True:
        valido = False
        loop = 0
        while loop < len(email):
            if "@" in email[loop]:
                while loop < len(email):
                    if "." in email[loop]:
                        if loop < len(email):
                            valido = True
                            break
                    loop += 1
            loop += 1
        print("Email inválido!")
        print("Tente --> email@dominio.com")
        email = input("Digite o email: ")


def NOME(nome):
    while True:
        valido = False
        if " " in nome:
            valido = True
            for num in Numbers:
                if str(num) in nome:
                    valido = False
        if valido == True:
            break
        else:
            print("Nome não está valido!")
            print("Tente --> Nome Sobrenome")
            nome = input("Digite nome: ")


nome = input("Digite nome: ")
NOME(nome)
email = input("Digite email: ")
EMAIL(email)
data = input("Digite data: ")
DATA(data)
