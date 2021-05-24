alunos = int(input("qual o numero de alunos?  "))
materias = int(input("qual o numero de matérias?  "))
lista = []
for i in range(alunos):
    notas = []
    nome = input("nome do aluno: ")
    for u in range(materias):
        nota = float(input("nota: ").replace(",", "."))
        notas.append(nota)
    media = round(sum(notas)/materias, 1)
    s = ''
    if media >= 7:
        s = "Aprovado"
    elif media >= 5:
        s = "Recuperação"
    else:
        s = "reprovado"
    lista.append((nome, [media, s]))
d = dict(lista)
print(d)
