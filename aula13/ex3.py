estoque_fixo = {"tomate": 1000, "alface": 500, "batata": 2001, "feijão": 100}
estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45],
           "batata": [2001, 1.20], "feijão": [100, 1.50]}
total = 0
print("____"*10)
print("SUPERMERCADO T2B")
print("____"*10)
while True:
    p = input("Digite o nome do produto para ser adquirido ou FIM p/ sair:")
    if p == "FIM":
        break
    if p in estoque:
        qtd = int(input("Digite a quantidade desse produto: "))
        if qtd <= estoque[p][0]:
            preco_u = estoque[p][2]
            custo = qtd*preco_u
            print(f"{p}:\t{qtd}\tx\t{preco_u:3.2f}\t=\t{custo:4.2f}")
            estoque[p][0] -= qtd
            total += custo
        elif estoque[p][0] == 0:
            print("Produto indisponivel")
        else:
            print("Quantidade não dispinivel")
    else:
        print("Produto Invalido")

print("")
print('___'*10)
print('COMPRA REALIZADA')
print('___'*10)
for k, v in estoque.items():
    if v[0] != estoque_fixo[k]:
        qtd = estoque_fixo[k] - v[0]
        custo = qtd*v[1]
        print(f"{k}:\t\t{qtd}\tx\tR$ {v[1]:6.2f}\t=\tR$ {custo:4.2f}")
print("____"*10)
print(f"Valor total da compra: R$ {total:6.2f}")
