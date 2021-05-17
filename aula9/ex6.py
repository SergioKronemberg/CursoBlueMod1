n = int(input("numero de matérias: "))
notas = []
for i in range(n):
    nota = float(input("digite a nota"))
    notas.append(nota)
media = sum(notas)/n
print("a media é: ", str(media))
