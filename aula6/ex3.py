def somaImposto(custo, taxa_imposto=10):
    return custo*taxa_imposto/100+custo


#t = float(input("insira porcentagem"))
x = float(input("insira custo"))
print(somaImposto(x))
