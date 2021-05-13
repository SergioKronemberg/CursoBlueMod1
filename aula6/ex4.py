def pagamento(qtd_horas, valor_hora=100):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    salario_base = 40*taxa
    if horas <= 40:
        salario = salario_base
    else:
        h_excd = horas - 40
        salario = salario_base+(h_excd*(1, 5*taxa))
    return salario


str_horas = input("dg as horas: ")
str_taxa = input("dg a taxa")
total_salario = pagamento(str_horas, str_taxa)
print(total_salario)
