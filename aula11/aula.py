listaCont = [('joao', '123-123'), ('bernardo', '456-456'), ('ricardo', '789=789'),
             ('gabriel', '101-101'), ('sergio', '112-112')]

contatos = dict(listaCont)
print(contatos)
nome = input("pesquisa: ").lower()
print(contatos.get(nome, "não encontrado"))
