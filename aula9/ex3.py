n = float((input("Preço do Pão: R$")).replace(",", "."))
print("Padaria Pão de Ontem - Tabela de preços:")
for i in range(1, 51):
    print(f"{i} - R$ {n*i:.2f}")
