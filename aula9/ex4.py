nomes = []

for i in range(1000):
    a = input("digite nome para acrescentar à lista ou 0 para sair: ").lower()
    if a == "0":
        break
    else:
        nomes.append(a)

nome = input("digite numero que deseja buscar").lower()
if nome in nomes:
    print("ok")
else:
    print("não ok")
