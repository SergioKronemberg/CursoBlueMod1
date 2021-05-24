nota = []
alunos = []
gabarito = ["a", "b", "c", "d", "e", "e", "d", "c", "b", "a"]
print('\n\t--- Área do Professor ---\n')
novo = input("Professor, deseja cadastrar um novo gabarito? S/N ").lower()
senha = "professor"
c = 0
while novo == 's':
    if input("Qual a senha? ").lower() == senha:
        for i in range(len(gabarito)):
            gabarito[i] = input(f"novo gabarito questão {i+1}: ").lower()
        break
    c += 1
    if c == 3:
        print("ACESSO NEGADO")
        break
print('\n\t---   Área do Aluno   ---\n')
while True:
    acertos = 0
    nome = input("Aluno, digite o seu nome: ")
    for questao in range(len(gabarito)):
        resposta = input(
            f'Digite a resposta da pergunta {questao + 1}: ').lower()
        if resposta == gabarito[questao]:
            acertos += 1
    nota.append(acertos)
    alunos.append(nome)
    continuar = input("Outro aluno vai utilizar o sistema? S/N ").lower()
    if continuar == 'n':
        break
print(f'Maior acerto: {max(nota)}')
print(f'Menor acerto: {min(nota)}')
print(f'Quantidade de alunos que utilizaram: {len(alunos)}')
print(f'A média da sala é: {sum(nota) / len(nota)} ')
