classe = dict()
for h in range(10):
    numero = input("numero do aluno: ")
    altura = int(input("altura: "))
    classe.update({numero: [altura]})
for k, v in classe.items():
    # vai printar a cond da 1ªkey true primeiro, se quisesse manter a ordem era só fazer dois fors
    if v == max(classe.values()):
        print(f"O nº{k} é o mais alto, com {v[0]}m")
    if v == min(classe.values()):
        print(f"O nº{k} é o mais baixo, com {v[0]}m")
