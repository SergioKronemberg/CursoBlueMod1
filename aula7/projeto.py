def custo_hotel(noites):
    return noites*140


def custo_aviao(cidade):
    if cidade == "SÃO PAULO":
        return 312
    if cidade == "PORTO ALEGRE":
        return 447
    if cidade == "RECIFE":
        return 831
    if cidade == "MANAUS":
        return 986


def custo_carro(dias):
    des = 0
    if dias >= 7:
        des = 50
    elif dias >= 3:
        des = 20
    return dias*40-des


def custo_total(cidade, dias, extra):
    total = custo_hotel(dias) + custo_carro(dias) + custo_aviao(cidade) + extra
    print(total)


c = input("cidade ").upper()
d = int(input("dias "))
e = int(input("gastos extras "))
custo_total(c, d, e)
