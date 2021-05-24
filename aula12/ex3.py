d = {}
alunos = int(input("qual o numero de alunos?  "))
for i in range(alunos):
    nome = input("nome do aluno: ")
    media = round(float(input("Media do aluno: ").replace(",", ".")), 1)
    if media >= 7:
        s = "Aprovado"
    elif media >= 5:
        s = "Recuperação"
    else:
        s = "reprovado"
    d.update({i: [nome, media, s]})
print(d)
