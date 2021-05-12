# Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

def menorNumero(a, b):
    if a < b:
        print(f"{a} é o menor")
    elif a == b:
        print("são iguais")
    else:
        print(f"{b} é o menor")


x = int(input("1º n:"))
y = int(input("2º n:"))
menorNumero(x, y)
