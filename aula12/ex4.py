from time import sleep
from random import randint
from operator import itemgetter
lista = []
for i in range(1, 5):
    dado = randint(1, 20)
    lista.append([f'jogador {i}', dado])
    if dado > 1:
        print(f'o jogador {i} tirou {dado} pontos ')
    else:
        print(f'o jogador {i} tirou {dado} ponto ')
    sleep(1)
dic = dict(lista)
dic2 = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(dic2)
