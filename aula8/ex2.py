
#palavra = "cerveja"
import random
lista = input("digite uma lista de palavra separadas por espaço: ")
lista = lista.split(" ")
palavra = random.choice(lista).lower()
palavra_forca = ["_" for i in palavra]
chance = 0
print("A palavra é: ", end=" ")
print(" ".join(palavra_forca))
# while palavra_forca.count("_")!=0 and chance !=6
# com while só retiraria as 3 linhas de baixo
maximo = len(palavra)+6
for i in range(maximo):
    if palavra_forca.count("_") == 0 or chance == 6:
        break
    letra = input("digite uma letra: ").lower()
    if letra in palavra_forca:
        print("Você ja usou essa letra antes, a palavra é: ", end=" ")
        print(" ".join(palavra_forca))
        continue
    if letra in palavra:
        print("A palavra é: ",
              end=" ")
        for n in range(len(palavra)):
            if letra == palavra[n]:
                palavra_forca[n] = letra
                # del palavra_forca[n]
                # palavra_forca.insert[n, letra]
        print(" ".join(palavra_forca))

    else:
        chance += 1
        print("voce errou pela ", str(chance), "a vez. Tente novamente")
if palavra_forca.count("_") == 0:
    print("Parabéns! você acertou a palavra!")
else:
    print("Forca! Você perdeu! xP")
