jogador = dict()
gols = []
jogador['nome'] = input("Nome do jogador: ")
total = int(input('Total de partidas: '))
for i in range(total):
    gols.append(int(input(f'Gols na partida {i+1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print("---"*10)
print("Jogador:", jogador['nome'])

print(f"{jogador['nome']} jogou {len(jogador['gols'])} partidas")
print("---"*10)

for k, v in enumerate(jogador['gols']):
    print(f'Na partida {k+1}, ele fez {v}gols')
print()
print(f"{jogador['nome']} fez {jogador['total']} no campeonato")
