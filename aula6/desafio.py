import datetime


def data(ano, mes, dia):
    x = datetime.datetime(dia, mes, ano)
    d = x.strftime("%d")
    m = x.strftime("%B")
    a = x.strftime("%Y")
    print(d, m, a)


d = int(input("Digite o dia: "))
m = int(input("Digite mês: "))
a = int(input("Digite o ano: "))


data(d, m, a)
