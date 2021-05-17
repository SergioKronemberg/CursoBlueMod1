print("Lojas Tabajara:")
x = []
p = float((input("Digite valor: R$")).replace(",", "."))
while p != 0:
    x.append(p)
    p = float((input("Digite valor: R$")).replace(",", "."))
print(f"Valor total: R${sum(x):.2f}")
c = float(input("Dinheiro fornecido: R$"))
print(f"Troco: R${c-sum(x):.2f}")
