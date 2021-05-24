from datetime import date
trabalhador = {}

nome = input("nome: ")
nasc = int(input("ano de nasc?"))
ctps = int(input('ctps: '))


def calcTrabalhador(nome, nascimento, ctps=0):
    idade = int(date.today().year) - nascimento
    if ctps == 0:
        anoContratacao = int(input("Informe o ano de contratação: "))
        salario = float(input(("Informe o valor do salário: ")))
        anoAposentadoria = (anoContratacao + 35) - nascimento
        trabalhador[nome] = {"Ano de nascimento": nascimento,
                             "Idade": idade,
                             "Idade de aposentadoria": anoAposentadoria}
    else:
        trabalhador[nome] = {"Ano de nascimento": nascimento, "Idade": idade}


calcTrabalhador(nome, nasc, ctps)
print(trabalhador)
