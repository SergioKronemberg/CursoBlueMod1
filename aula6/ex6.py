def letraNota(nota):
    if nota < 0 or nota > 10:
        return "nota invalida"
    elif nota >= 9:
        return "A"
    elif nota >= 8:
        return "B"
    elif nota >= 7:
        return "C"
    elif nota >= 6:
        return "D"
    elif nota <= 4:
        return "F"


c = float(input("nota: ").replace(",", "."))
print(letraNota(c))
