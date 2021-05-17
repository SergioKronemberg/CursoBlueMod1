n = int(input("digite um num int: "))

contador = 0
# divisores=[]
for i in range(n, 0, -1):
    if(n % i == 0):
        # divisores.append(i)
        print(i)
        contador += 1
if contador == 2:
    # if len(divisores)==2
    print(n, "é um num primo!")
