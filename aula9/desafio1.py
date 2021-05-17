from random import randint
tentativas = 0
r = randint(1, 100)
a = int(input("advinhe um n entre 1 e 100:  "))
while a != r:
    print("incorreto")
    a = int(input("advinhe um n entre 1 e 100:  "))
    tentativas += 1
    if tentativas == 10:
        print("o numero era:", r)
        break
