# – Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois.
# Enquanto a soma não for 50, ele deve continuar repetindo

x = int(input("1º:  "))
y = int(input("2º:  "))
while x+y != 50:
    print("=", x+y)
    x = int(input("1º:  "))
    y = int(input("2º:  "))
print("= 50! ")
