'''Crie um programa que tenha uma função chamada voto () 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, 
pesquise sobre a função date da biblioteca Datetime.'''
from datetime import date
ano = int(input("Qual ano você nasceu?: "))


def voto(X):
    if X > date.today().year - 16:
        return "NEGADO"
    elif date.today().year - 16 >= X > date.today().year - 18 or X <= date.today().year - 70:
        return "OPCIONAL"
    else:
        return "OBRIGATORIO"


print(voto(ano))
