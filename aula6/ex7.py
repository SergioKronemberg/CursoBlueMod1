def menor(a, b):
    if a < b:
        print("menor é", a)
    elif a == b:
        print("são iguais")
    else:
        print("menor é", b)


x = int(input("entrada1: "))
y = int(input("entrada2: "))
menor(x, y)
