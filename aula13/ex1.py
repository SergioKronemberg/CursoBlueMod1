aniv = {}
while True:
    nome = input("Digite o nome da celebridade e 0 pra sair: ")
    if nome == "0":
        break
    data = input('Digite a data de nascimento da celebridade (dd/mm/yyyy): ')
    sexo = input('Digite o Sexo da celebridade:')
    aniv[nome] = [data, sexo]
print('---------------------')
for k, v in aniv.items():
    print(f'{k}\t-\t {v[0]}\t-\t{v[1]}')  # \t tab
print('---------------------')
nome = input('Digite nome da celebridade e descubra a data de nasc: ')
print(aniv.get(nome, ' não cadastrada'))

for k, v in aniv.items():
    print(f'{k}\t-\t {v[0]}\t-\t{v[1]}')  # \t tab
