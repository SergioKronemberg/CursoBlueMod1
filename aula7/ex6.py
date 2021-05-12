'''Um professor, muito legal, fez 3 provas durante um semestre,
 mas só vai levar em conta as duas notas mais altas para calcular a média.

Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas,
a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.'''


def media3(x, y, z):
    media1 = (x+y+z)/3
    if x < y and x < z:
        menor = x
    elif y < x and y < z:
        menor = y
    else:
        menor = z
    if x > y and x > z:
        maior = x
    elif y > x and y > z:
        maior = y
    else:
        maior = z
    media2 = (x+y+z-menor)/2
    return print(f"media original:{media1:.1f}\nmedia aplicada:{media2:.1f}\nnota mais alta:{maior:.1f}\nnota mais baixa:{menor:.1f}")


a = float(input("1ª nota: ").replace(",", "."))
b = float(input("2ª nota: ").replace(",", "."))
c = float(input("3º nota: ").replace(",", "."))
media3(a, b, c)
