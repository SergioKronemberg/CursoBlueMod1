'''Escreva uma função que recebe dois números (a e b) como parâmetro
 e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''


def somaMaior21(a, b):
    limite = 21
    if a+b > limite:
        return True
    else:
        return False


x = int(input("1º n:"))
y = int(input("2º n:"))
print(somaMaior21(x, y))
