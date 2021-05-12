'''Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(n, g):
    print(f" jogador {n}, marcou {g} gols")


nome = input("nome do jogador: ")
gols = input("nº de gols: ")
ficha(nome, gols)
