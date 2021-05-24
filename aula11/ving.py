ving = {'Chris Evans': 'Cap. América', 'Mark Ruffalo': 'Hulk', 'Robert Downey Jr': 'Homem de Ferro',
        'Scarlett Johansson': 'Viúva Negra', 'Tom Hiddleston': 'Loki', 'Chris Hemworth': 'Thor'}
# pesquisa = input("Pesquisa: ").title()
# print(ving.get(pesquisa, "Não encontrado"))
# print(ving.keys())
# print(ving.values())
ving["Gal Gadot"] = "Mulher Maravillha"
ving["Tom Holand"] = "Homem-aranha"
ving["Hugh Jackman"] = "Wolverine"
print(ving)
# del ving["Gal Gadot"]
# igual mas o pop retorna o values da key
print(ving.pop("Gal Gadot", "nao encontrado"))
print()
print(ving)
outros = {"Rian Reinaldo": "Deadpool",
          "Roberto Bolanhos": "Chapolim", "Kakaroto": "Goku"}
# for i in outros:
#     ving[i] = outros[i]
ving.update(outros)
print()
print(ving)
